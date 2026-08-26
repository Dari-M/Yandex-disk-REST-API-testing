from yandex_api.api_client import YandexDiskClient

#PATCH-01: Перезапись существующего custom_property
def test_patch_overwrite_custom_property():
    client = YandexDiskClient()
    path = "disk:/autotests"
    response = client.update_custom_properties(
        path,
        {"qa_test": "old"}
    )

    assert response.status_code == 200
    assert response.json()["custom_properties"]["qa_test"] == "old"

    response = client.update_custom_properties(
        path,
        {"qa_test": "new"}
    )

    assert response.status_code == 200

    data = response.json()

    assert data["custom_properties"]["qa_test"] == "new"

    response = client.update_custom_properties(
        path,
        {"qa_test": None}
    )

    assert response.status_code == 200

#PATCH-01: Удаление существующего custom_property
def test_delete_custom_property():
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
    data =  response.json()
    assert data["custom_properties"] is None
