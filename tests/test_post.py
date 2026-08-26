from yandex_api.api_client import YandexDiskClient

#POST-01: Загрузка файла по URL в несуществующий путь
def test_upload_file_to_nonexistent_path():
    client = YandexDiskClient()
    file_url = "https://en.wikipedia.org/wiki/Duck#/media/File:Bucephala-albeola-010.jpg"
    invalid_path = "disk:/autotests/nonexistent_folder/test_file.jpg"
    response = client.upload_by_url(file_url, invalid_path)

    assert response.status_code == 409

    data = response.json()

    assert data["error"] == "DiskPathDoesntExistsError"

#POST-01: Перемещение несуществующего ресурса
def test_move_nonexistent_resource():
    client = YandexDiskClient()
    nonexistent_path = "disk:/autotests/nonexistent_file.txt"
    destination = "disk:/autotests"

    response = client.move_resource(
        nonexistent_path,
        destination
    )

    assert response.status_code == 404

    data = response.json()

    assert data["error"] == "DiskNotFoundError"
