from yandex_api.api_client import YandexDiskClient

# DELETE-01: Удаления несуществующего ресурса (Negative)
def test_delete_nonexistent_resource():
    client = YandexDiskClient()
    path = "disk:/autotests/nonexistent_delete_test"

    response = client.delete_resource(path)

    assert response.status_code == 404

    data = response.json()

    assert data["error"] == "DiskNotFoundError"

# DELETE-02: Удаление корневой папки (Boundary / Negative)
def test_delete_root_folder():
    client = YandexDiskClient()
    path = "disk:/"

    response = client.delete_resource(path)

    assert response.status_code == 409

    data = response.json()

    assert data["error"] == "DiskPathDoesntExistsError"
