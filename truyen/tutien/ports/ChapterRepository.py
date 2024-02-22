from abc import ABC, abstractmethod
from typing import List
from core.models import Chapter

class ChapterRepository(ABC):
    @abstractmethod
    def create_chapter(self, chapter: Chapter) -> Chapter:
        pass

    @abstractmethod
    def read_chapter_by_id(self, chapter_id: int) -> Chapter:
        pass

    @abstractmethod
    def read_chapters_of_story(self, story_id: int) -> List[Chapter]:
        pass

    @abstractmethod
    def update_chapter(self, chapter_id: int, updated_chapter: Chapter) -> Chapter:
        pass

    @abstractmethod
    def delete_chapter(self, chapter_id: int):
        pass