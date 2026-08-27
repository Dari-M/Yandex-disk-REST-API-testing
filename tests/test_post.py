from yandex_api.api_client import YandexDiskClient

# POST-01: Загрузка файла по URL в несуществующий путь (Negative)
def test_upload_file_to_nonexistent_path():
    client = YandexDiskClient()
    file_url = "https://en.wikipedia.org/wiki/Duck#/media/File:Bucephala-albeola-010.jpg"
    invalid_path = "disk:/autotests/nonexistent_folder/test_file.jpg"
    response = client.upload_by_url(file_url, invalid_path)

    assert response.status_code == 409

    data = response.json()

    assert data["error"] == "DiskPathDoesntExistsError"

# POST-02: Перемещение ресурса в тот же путь (Boundary)
def test_move_resource_to_same_path():
    client = YandexDiskClient()
    path = "disk:/autotests/post_test"

    create_response = client.create_folder(path)
    assert create_response.status_code == 201

    try:
        response = client.move_resource(
            path,
            path
        )

        assert response.status_code == 409

        data = response.json()

        assert data["error"] == "DiskPathDoesntExistsError"

    finally:
        delete_response = client.delete_resource(path)
        assert delete_response.status_code in (202, 204)
