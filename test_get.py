from yandex_api.api_client import YandexDiskClient

# GET-01: Получение метаинформации несуществующего ресурса (Negative)
def test_get_nonexistent_resource():
    client = YandexDiskClient()
    path = "disk:/autotests/nonexistent_folder/test_file.jpg"

    response = client.get_resource(path)

    assert response.status_code == 404
    assert response.json()["error"] == "DiskNotFoundError"

# GET-02: Получение cодержимого пустой корзины (Boundary)
def test_get_empty_trash():
    client = YandexDiskClient()

    response = client.get_trash()

    assert response.status_code == 200

    data = response.json()

    assert data["path"] == "trash:/"
    assert data["type"] == "dir"
    assert data["name"] == "trash"

    assert data["_embedded"]["path"] == "trash:/"
    assert data["_embedded"]["total"] == 0
    assert data["_embedded"]["items"] == []