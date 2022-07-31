from src.dataclasses.asset_data import AssetData


def test_content_data_id():
    data = AssetData(filename="/a/b/c.png")
    assert data.id == "a-b-c"


def test_content_data_ext():
    data = AssetData(filename="/a/b/c.jpg")
    assert data.ext == ".jpg"
