import os
import requests

class YandexDiskClient:

    BASE_URL = "https://cloud-api.yandex.net/v1/disk"

    def __init__(self):
        token = os.getenv("YANDEX_TOKEN")
        if not token:
            raise ValueError("YANDEX_TOKEN не найден")
        self.headers = {
            "Authorization": f"OAuth {token}"
        }

    def get_resource(self, path):
        return requests.get(
            f"{self.BASE_URL}/resources",
            headers=self.headers,
            params={
                "path": path
            }
        )

    def create_folder(self, path):
        return requests.put(
            f"{self.BASE_URL}/resources",
            headers=self.headers,
            params={
                "path": path
            }
        )

    def delete_resource(self, path):
        return requests.delete(
            f"{self.BASE_URL}/resources",
            headers=self.headers,
            params={
                "path": path,
                "permanently": "true"
            }
        )

    def upload_by_url(self, url, path):
        return requests.post(
            f"{self.BASE_URL}/resources/upload",
            headers=self.headers,
            params={
                "url": url,
                "path": path
            }
        )

    def update_custom_properties(self, path, custom_properties):
        return requests.patch(
            f"{self.BASE_URL}/resources",
            headers=self.headers,
            params={
                "path": path
            },
            json={
                "custom_properties": custom_properties
            }
        )

    def move_resource(self, path, destination):
        return requests.post(
            f"{self.BASE_URL}/resources/move",
            headers=self.headers,
            params={
                "from": path,
                "path": destination
            }
        )

    def get_operation(self, href):
        return requests.get(
            href,
            headers=self.headers
        )

    def get_trash(self):
        return requests.get(
            f"{self.BASE_URL}/trash/resources",
            headers=self.headers,
            params={
                "path": "trash:/"
            }
        )
