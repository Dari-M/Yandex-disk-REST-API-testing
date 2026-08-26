from yandex_api.api_client import YandexDiskClient

#PUT-01: Создание ресурса по существующему пути
def test_create_folder_with_existing_path():
    client = YandexDiskClient()
    test_path = "disk:/autotests/put_test"
    create_response = client.create_folder(test_path)
    assert create_response.status_code == 201

    try:
        response = client.create_folder(test_path)
        assert response.status_code == 409
        data = response.json()
        assert data["error"] == "DiskPathPointsToExistentDirectoryError"

    finally:
        delete_response = client.delete_resource(test_path)
        assert delete_response.status_code == 204

#PUT-02: Создание ресурса с именем "."
def test_create_folder_with_dot():
    client = YandexDiskClient()
    path = "disk:/autotests/."

    response = client.create_folder(path)

    assert response.status_code == 404
    assert response.json()["error"] == "DiskNotFoundError"

#PUT-03: Создание ресурса с расширением файла в имени
def test_create_folder_with_file_extension():
    client = YandexDiskClient()
    path = "disk:/autotests/test.jpg"
    response = client.create_folder(path)

    assert response.status_code == 201

    response = client.get_resource(path)

    assert response.status_code == 200

    data = response.json()

    assert data["path"] == path
    assert data["type"] == "dir"
    assert data["name"] == "duck.jpg"

    response = client.delete_resource(path)

    assert response.status_code in (202, 204)
