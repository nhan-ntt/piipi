from sqlalchemy.orm import Session
from core.models import Genre
from typing import List
from ports.GenreRepository import GenreRepository

class PostgresGenreRepository(GenreRepository):
    def __init__(self, session: Session):
        self.session = session

    def create_genre(self, title: str) -> Genre:
        new_genre = Genre(title=title)
        self.session.add(new_genre)
        self.session.commit()
        self.session.refresh(new_genre)
        return new_genre

    def get_genre(self, genre_id: int) -> Genre:
        return self.session.query(Genre).filter(Genre.id == genre_id).first()

    def get_all_genres(self) -> List[Genre]:
        return self.session.query(Genre).all()

    def update_genre(self, genre_id: int, updated_genre: Genre) -> Genre:
        existing_genre = self.session.query(Genre).filter(Genre.id == genre_id).first()
        if existing_genre:
            existing_genre.title = updated_genre.title

            self.session.commit()
        return existing_genre

    def delete_genre(self, genre_id: int):
        self.session.query(Genre).filter(Genre.id == genre_id).delete()
        self.session.commit()

