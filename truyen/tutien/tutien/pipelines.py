
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from core.models import Story, Chapter, Genre, Base
from sqlalchemy.ext.declarative import declarative_base
from .items import StoryItem, ChapterItem, GenreItem
from scrapy.exceptions import DropItem

DATABASE_URL = "postgresql://postgres:thanhnhan1911@localhost:5432/nhon"
# DATABASE_URL = "postgresql://postgres:thanhnhan1911@localhost:5432/nhon?charset=utf8mb4"

class TutienPipeline:
    # pass
    def __init__(self):
        engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        if isinstance(item, GenreItem):
            self.store_genre(item)
        elif isinstance(item, StoryItem):
            self.store_story(item)
        elif isinstance(item, ChapterItem):
            self.store_chapter(item)
        return item

        # self.store_story(item)
        # self.store_chapter(item)

    def store_genre(self, item):
        with self.Session() as session:
            try:
                genre = Genre(
                    title=item['title'],
                    code=item['code'],
                )
                session.add(genre)
                session.commit()
                print("genre okekekeke")
            except Exception as e:
                session.rollback()
                raise DropItem(f"Failed to store genre: {e}")

    def store_story(self, item):
        with self.Session() as session:
            try:
                story = Story(
                    title=item['title'], 
                    author=item['author'], 
                    description=item['description'][:255],
                    code=item['code'],
                    genre_id=item['genre_id']
                )
                session.add(story)
                session.commit()
                print("story okekekeke")
            except Exception as e:
                session.rollback()
                raise DropItem(f"Failed to store story: {e}")

    def store_chapter(self, item):
        with self.Session() as session:
            try:
                chapter = Chapter(
                    title=item['title'], 
                    content=item['content'][:255],
                    story_id=item['story_id']
                )
                session.add(chapter)
                print("chapter okekekeke")
                session.commit()
            except Exception as e:
                session.rollback()
                raise DropItem(f"Failed to store chapter: {e}")
