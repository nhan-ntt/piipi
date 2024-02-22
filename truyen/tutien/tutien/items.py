# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutienItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


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


class ChapterItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    story_id = scrapy.Field()