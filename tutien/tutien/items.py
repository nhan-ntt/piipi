# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class GenreItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    code = scrapy.Field()


class StoryItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    description = scrapy.Field()
    code = scrapy.Field()
    genre_id = scrapy.Field()
    img_url = scrapy.Field()


class ChapterItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    story_id = scrapy.Field()


class ImageItem(scrapy.Item):
    images = scrapy.Field()
    image_urls = scrapy.Field()