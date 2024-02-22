from abc import ABC, abstractmethod
from typing import List
from core.models import Story

class StoryRepository(ABC):
    @abstractmethod
    def create_story(self, story: Story) -> Story:
        pass

    @abstractmethod
    def read_story_by_id(self, story_id: int) -> Story:
        pass

    @abstractmethod
    def read_stories_of_genre(self, genre_id: int) -> List[Story]:
        pass
    
    @abstractmethod
    def update_story(self, story_id: int, updated_story: Story) -> Story:
        pass

    @abstractmethod
    def delete_story(self, story_id: int):
        pass