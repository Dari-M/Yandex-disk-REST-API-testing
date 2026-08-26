from yandex_api.api_client import YandexDiskClient

#DELETE-01: Удаления ресурса без перемещения в корзину
def test_delete_resource_permanently():
    client = YandexDiskClient()

    base_path = "disk:/autotests"
    path = "disk:/autotests/delete_test"

    response = client.get_resource(base_path)

    if response.status_code == 404:
        response = client.create_folder(base_path)
        assert response.status_code == 201

    response = client.create_folder(path)
    assert response.status_code == 201

    response = client.delete_resource(path)
    assert response.status_code in (202, 204)

    if response.status_code == 202:
        operation_href = response.json()["href"]

        response = client.get_operation(operation_href)

        assert response.status_code == 200
        assert response.json()["status"] == "success"

    response = client.get_resource(path)

    assert response.status_code == 404

    response = client.get_trash()

    assert response.status_code == 200

    data = response.json()

    assert data["_embedded"]["total"] == 0
    assert data["_embedded"]["items"] == []

#DELETE-02: Удаления несуществующего ресурса
def test_delete_nonexistent_resource():
    client = YandexDiskClient()
    path = "disk:/autotests/nonexistent_delete_test"

    response = client.delete_resource(path)

    assert response.status_code == 404

    data = response.json()

    assert data["error"] == "DiskNotFoundError"