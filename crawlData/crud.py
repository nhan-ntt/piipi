from database import engine
from models import Story, Chapter
from database import session


# Create (Insert)

def create_story(title, description, author):
    new_story = Story(title=title, description=description, author=author)
    session.add(new_story)
    session.commit()
    return new_story

def create_chapter(title, content, story_id):
    new_chapter = Chapter(title=title, content=content, story_id=story_id)
    session.add(new_chapter)
    session.commit()
    return new_chapter

# Read (Select)
def read_story(story_id):
    return session.query(Story).filter(Story.id == story_id).first()

# list all stories
def read_all_stories():
    return session.query(Story).all()

# all chapters of a story
def read_chapters_of_story(story_id):
    return session.query(Chapter).filter(Chapter.story_id == story_id).all()

def read_story_by_chapter(story_id, chapter_id):
    chapter = session.query(Chapter).filter(id=chapter_id, story_id=story_id).first()
    if chapter:
        return chapter.content
    return None


# Update (Update)
def update_story(story_id, n_title, n_description, n_author):
    story = session.query(Story).filter(id == story_id).first()
    if story:
        story.title = n_title
        story.description = n_description
        story.author = n_author
        session.commit()
    return story

def update_chapter(chapter_id, n_title, n_content):
    chapter = session.query(Chapter).filter(id == chapter_id).first()
    if chapter:
        chapter.title = n_title
        chapter.content = n_content
        session.commit()
    return chapter

# Delete (Delete)

def delete_story(story_id):
    story = session.query(Story).filter(id == story_id).first()
    if story:
        session.delete(story)
        session.commit()

def delete_chapter(chapter_id):
    chapter = session.query(Chapter).filter(id == chapter_id).first()
    if chapter:
        session.delete(chapter)
        session.commit()

if __name__ == '__main__':
    a = create_story('title', 'description', 'aadfasfuthor')
    print(a.author)