from sqlalchemy import Column, Integer, String, ForeignKey, Index
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Genre(Base):
    __tablename__ = 'genre'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False, index=True)
    code = Column(String(255), nullable=False, unique=True)

    stories = relationship("Story", back_populates="genre")


class Story(Base):
    __tablename__ = 'story'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False, index=True)
    description = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    code = Column(String(255), nullable=False, unique=True)
    genre_id = Column(Integer, ForeignKey('genre.id'), nullable=False, index=True)

    genre = relationship("Genre", back_populates="stories")
    chapters = relationship("Chapter", back_populates="story")

class Chapter(Base):
    __tablename__ = 'chapter'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False, index=True)
    content = Column(String(255), nullable=False)
    story_id = Column(Integer, ForeignKey('story.id'), nullable=False, index=True)
    
    story = relationship("Story", back_populates="chapters")
