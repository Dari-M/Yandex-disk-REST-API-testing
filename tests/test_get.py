from yandex_api.api_client import YandexDiskClient

#GET-01: Получение  метаданных существующего ресурса
def test_get_resource():
    client = YandexDiskClient()
    test_path = "disk:/autotests/get_test"
    create_response = client.create_folder(test_path)
    assert create_response.status_code == 201

    try:
        response = client.get_resource(test_path)
        assert response.status_code == 200
        data = response.json()
        assert data["path"] == test_path
        assert data["type"] == "dir"
        assert data["name"] == "get_test"

    finally:
        delete_response = client.delete_resource(test_path)
        assert delete_response.status_code == 204

#GET-02: Получение несуществующего ресурса
def test_get_nonexistent_resource():
    client = YandexDiskClient()
    path = "disk:/autotests/nonexistent_folder/test_file.jpg"

    response = client.get_resource(path)

    assert response.status_code == 404
    assert response.json()["error"] == "DiskNotFoundError"
