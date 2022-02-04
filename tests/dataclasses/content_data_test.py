

from src.dataclasses.content_data import ContentData


def test_content_data_is_md():
  data = ContentData(filename="test.hbs")
  assert(data.is_md == False)

  data = ContentData(filename="test.md")
  assert(data.is_md == True)

def test_content_data_slug():
  data = ContentData(filename="test.hbs")
  assert(data.slug == "test.html")

  data = ContentData(
    filename="test.hbs",
    meta={ "slug": "abc" }
  )
  assert(data.slug == "abc.html")

def test_content_data_title():
  data = ContentData(filename="Test.md")
  assert(data.title == "Test")

  data = ContentData(filename="Parent - Child.md")
  assert(data.title == "Child")

  data = ContentData(filename="Parent - Children - Child.md")
  assert(data.title == "Child")

  data = ContentData(meta={ "title": "Title"})
  assert(data.title == "Title")

