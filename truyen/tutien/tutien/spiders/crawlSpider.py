import scrapy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from ..items import TutienItem, StoryItem, ChapterItem, GenreItem
from slugify import slugify
# import slugify.slugify
from core import models
import time

class MySpider(scrapy.Spider):
    name = 'hehe'
    start_urls = [
        # 'https://truyen.tangthuvien.vn/doc-truyen/dai-phung-da-canh-nhan',
        'https://truyenfull.vn/',
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        engine = create_engine('postgresql://postgres:thanhnhan1911@localhost:5432/nhon')
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def parse(self, response):
        all_genres = response.css(".row .col-xs-6 a")
        for genre in all_genres:
            genre_url = genre.css('::attr(href)').extract_first()
            yield scrapy.Request(genre_url, callback=self.parse_genre)

    def parse_genre(self, response):
        genre_item = GenreItem()
        genre_item['title'] = response.css('li.active a span::text').get()
        genre_item['code'] = slugify(response.url.split('/')[-2])
        # yield genre_item

        all_stories = response.css(".col-xs-7 h3.truyen-title a")
        for story in all_stories:
            story_url = story.css('::attr(href)').extract_first()
            yield scrapy.Request(
                story_url,
                callback=self.parse_story,
                meta={'genre_code': genre_item['code']}
            )

    def parse_story(self, response):
        genre_code = response.meta['genre_code']

        story_item = StoryItem()
        story_item['title'] = response.css('div.col-info-desc h3.title::text').get()
        story_item['author'] = response.css('div.col-info-desc a[itemprop="author"]::text').get()

        description = response.css('.desc-text::text').getall()
        story_item['description'] = ' '.join(description).strip()

        story_item['code'] = slugify(response.url.split('/')[-2])

        _genre = self.get_genre_by_code(genre_code)
        story_item['genre_id'] = _genre.id
        # yield story_item

        # Extract chapter titles and content
        all_chapters = response.css('ul.list-chapter li')

        for chapter in all_chapters:
            chapter_url = chapter.css('::attr(href)').extract_first()

            yield scrapy.Request(
                chapter_url,
                callback=self.parse_chapter,
                meta={'story_code': story_item['code']}
            )

    def parse_chapter(self, response):
        story_code = response.meta['story_code']
        print("story codeeee", story_code)

        chapter_item = ChapterItem()

        chapter_item['title'] = response.css(".col-xs-12 a::text").get()
        paragraphs = response.css('.chapter-c p').extract()
        merged_content = ''

        for paragraph in paragraphs:
            merged_content += ' '.join(
                paragraph.split('<br>')) + '\n'  # Merge text separated by <br> tags and add newline

        chapter_item['content'] = merged_content

        _story = self.get_story_by_code(story_code)
        chapter_item['story_id'] = _story.id
        # time.sleep(5)
        yield chapter_item

    def get_genre_by_code(self, code):
        return self.session.query(models.Genre).filter(models.Genre.code == code).first()

    def get_story_by_code(self, code):
        return self.session.query(models.Story).filter(models.Story.code == code).first()