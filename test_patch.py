from yandex_api.api_client import YandexDiskClient

# PATCH-01: Изменение custom_property несуществующего ресурса (Negative)
def test_update_custom_property_for_nonexistent_resource():
    client = YandexDiskClient()
    path = "disk:/autotests/nonexistent_patch_test"

    response = client.update_custom_properties(
        path,
        {"qa_test": "value"}
    )

    assert response.status_code == 404

    data = response.json()

    assert data["error"] == "DiskNotFoundError"

# PATCH-02: Передача null для существующего custom_property (Boundary)
def test_set_custom_property_to_null():
    client = YandexDiskClient()
    path = "disk:/autotests"

    response = client.update_custom_properties(
        path,
        {"qa_test": "old"}
    )

    assert response.status_code == 200

    response = client.get_resource(path)
    assert response.status_code == 200

    data = response.json()
    assert data["custom_properties"]["qa_test"] == "old"

    response = client.update_custom_properties(
        path,
        {"qa_test": None}
    )

    assert response.status_code == 200

    data = response.json()
    assert data["custom_properties"] is None