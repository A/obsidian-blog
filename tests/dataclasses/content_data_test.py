from src.dataclasses.content_data import ContentData


def test_content_data_ext():
    data = ContentData(filename='test.hbs')
    assert data.ext == '.hbs'

    data = ContentData(filename='test.md')
    assert data.ext == '.md'


def test_content_data_slug():
    data = ContentData(filename='test.hbs')
    assert data.slug == 'test.html'

    data = ContentData(filename='test.hbs', meta={'slug': 'abc'})
    assert data.slug == 'abc.html'


def test_content_data_title():
    data = ContentData(filename='Test.md')
    assert data.title == 'Test'

    data = ContentData(filename='Parent - Child.md')
    assert data.title == 'Child'

    data = ContentData(filename='Parent - Children - Child.md')
    assert data.title == 'Child'

    data = ContentData(meta={'title': 'Title'})
    assert data.title == 'Title'


def test_content_data_is_private():
    data = ContentData(meta={'published': True})
    assert data.is_private == False

    data = ContentData(meta={'published': False})
    assert data.is_private == True

    data = ContentData(meta={})
    assert data.is_private == True


def test_content_data_id():
    data = ContentData(filename='/a/b/c.md')
    assert data.id == 'a-b-c'


def test_content_data_sorting():
    arr = [
        ContentData(
            meta={
                'date': '2022-01-01',
                'title': '1',
            }
        ),
        ContentData(meta={'date': '2022-01-02', 'title': '2'}),
    ]

    arr_sorted = sorted(arr, reverse=True)

    assert list(map(lambda i: i.title, arr_sorted)) == ['1', '2']
