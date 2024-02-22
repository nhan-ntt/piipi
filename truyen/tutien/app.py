from fastapi import FastAPI, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

from core.models import Story, Chapter
from core.schemas import StorySchema, ChapterSchema
from adapters.PostgresStoryRepository import PostgresStoryRepository 
from adapters.PostgresChapterRepository import PostgresChapterRepository

from core.models import Base

DATABASE_URL = "postgresql://postgres:thanhnhan1911@localhost:5432/nhon"
# DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

Sessionlocal = sessionmaker(bind=engine)

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

# Dependency to get the story repository
def get_story_repository(db: Session = Depends(get_db)):
    return PostgresStoryRepository(db)

# Dependency to get the chapter repository
def get_chapter_repository(db: Session = Depends(get_db)):
    return PostgresChapterRepository(db)

# API routes for Story
@app.post("/stories/", response_model=dict)
def create_story(
    story: StorySchema,
    story_repo: PostgresStoryRepository = Depends(get_story_repository)
):
    return story_repo.create_story(
        title=story.title,
        description=story.description,
        author=story.author
    )

@app.get("/stories/{story_id}", response_model=None)
def read_story(
    story_id: int, 
    story_repo: PostgresStoryRepository = Depends(get_story_repository)
):
    return story_repo.read_story_by_id(story_id)

@app.get("/stories/", response_model=None)
def read_all_stories(story_repo: PostgresStoryRepository = Depends(get_story_repository)):
    return story_repo.read_all_stories()

@app.put("/stories/{story_id}", response_model=None)
def update_story(
    story_id: int, 
    updated_story: StorySchema, 
    story_repo: PostgresStoryRepository = Depends(get_story_repository)
):
    return story_repo.update_story(story_id, updated_story)

@app.delete("/stories/{story_id}")
def delete_story(
    story_id: int, 
    story_repo: PostgresStoryRepository = Depends(get_story_repository)
):
    story_repo.delete_story(story_id)
    return {"message": "Story deleted successfully"}

# API routes for Chapter
@app.post("/chapters/", response_model=None)
def create_chapter(
    chapter: ChapterSchema, 
    chapter_repo: PostgresChapterRepository = Depends(get_chapter_repository)
):
    return chapter_repo.create_chapter(
        story_id=chapter.story_id,
        title=chapter.title,
        content=chapter.content
    )


@app.get("/chapters/{chapter_id}", response_model=None)
def read_chapter(
    story_id: int,
    chapter_id: int, 
    chapter_repo: PostgresChapterRepository = Depends(get_chapter_repository)
):
    return chapter_repo.read_chapter_by_id(chapter_id)

# @app.get("/chapters/story/{story_id}", response_model=None)
# def read_chapters_of_story(story_id: int, chapter_repo: PostgresChapterRepository = Depends(get_chapter_repository)):
#     return chapter_repo.read_chapters_of_story(story_id)

# @app.put("/chapters/{chapter_id}", response_model=None)
# def update_chapter(chapter_id: int, updated_chapter: Chapter, chapter_repo: PostgresChapterRepository = Depends(get_chapter_repository)):
#     return chapter_repo.update_chapter(updated_chapter)

# @app.delete("/chapters/{chapter_id}")
# def delete_chapter(chapter_id: int, chapter_repo: PostgresChapterRepository = Depends(get_chapter_repository)):
#     chapter_repo.delete_chapter(chapter_id)
#     return {"message": "Chapter deleted successfully"}