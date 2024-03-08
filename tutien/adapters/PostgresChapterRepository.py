from sqlalchemy import or_
from sqlalchemy.orm import Session
from core.models import Chapter, Story
from ports.ChapterRepository import ChapterRepository
from typing import List


class PostgresChapterRepository(ChapterRepository):
    def __init__(self, session: Session):
        self.session = session

    def create_chapter(self, story_id: int, title: str, content: str) -> Chapter:
        new_chapter = Chapter(story_id=story_id, title=title, content=content)
        self.session.add(new_chapter)
        self.session.commit()
        self.session.refresh(new_chapter)
        return new_chapter

    def read_chapter_by_id(self, story_id: int, chapter_id: int) -> Chapter:
        # return self.session.query(Chapter).filter(Chapter.id == chapter_id).first()
        return self.session.query(Chapter).filter_by(story_id=story_id, id=chapter_id).first()

    def read_chapters_of_story(self, story_id: int) -> List[Chapter]:
        return self.session.query(Chapter).join(Story).filter(Story.id == story_id).all()

    def update_chapter(self, chapter_id: int, updated_chapter: Chapter) -> Chapter:
        existing_chapter = self.session.query(Chapter).filter(Chapter.id == chapter_id).first()
        if existing_chapter:
            existing_chapter.title = updated_chapter.title
            existing_chapter.content = updated_chapter.content

            self.session.commit()
        return existing_chapter

    def delete_chapter(self, chapter_id: int):
        self.session.query(Chapter).filter(Chapter.id == chapter_id).delete()
        self.session.commit()
