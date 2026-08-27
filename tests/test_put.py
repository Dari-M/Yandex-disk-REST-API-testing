from yandex_api.api_client import YandexDiskClient

# PUT-01: Создание ресурса по несуществующему пути (Negative)
def test_create_folder_with_nonexistent_path():
    client = YandexDiskClient()
    test_path = "disk:/autotests/nonexistent_folder/new_folder"

    response = client.create_folder(test_path)

    assert response.status_code == 409

    data = response.json()

    assert data["error"] == "DiskPathDoesntExistsError"

# PUT-02: Создание ресурса с именем "." (Boundary)
def test_create_folder_with_dot():
    client = YandexDiskClient()
    path = "disk:/autotests/."

    response = client.create_folder(path)

    assert response.status_code == 404
    assert response.json()["error"] == "DiskNotFoundError"
