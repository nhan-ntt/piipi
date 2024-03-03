from abc import ABC, abstractmethod
from typing import List
from core.models import Genre

class GenreRepository(ABC):
    @abstractmethod
    def create_genre(self, genre: Genre) -> Genre:
        pass

    @abstractmethod
    def get_genre(self, genre_id: int) -> Genre:
        pass

    @abstractmethod
    def get_all_genres(self) -> List[Genre]:
        pass

    @abstractmethod
    def update_genre(self, genre_id: int, updated_genre: Genre) -> Genre:
        pass

    @abstractmethod
    def delete_genre(self, genre_id: int):
        pass