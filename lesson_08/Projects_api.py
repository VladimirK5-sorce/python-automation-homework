import requests


class ProjectsApi:
    def __init__(self, url: str, token: str):
        self.url = url
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def create_project(self, title: str, users: dict = None):
        payload = {"title": title}
        if users is not None:
            payload["users"] = users
        return requests.post(
            f"{self.url}/api-v2/projects",
            json=payload,
            headers=self.headers
        )

    def get_project(self, project_id: str):
        return requests.get(
            f"{self.url}/api-v2/projects/{project_id}",
            headers=self.headers
        )

    def update_project(
        self, project_id: str, title: str = None, deleted: bool = None
    ):
        payload = {}
        if title is not None:
            payload["title"] = title
        if deleted is not None:
            payload["deleted"] = deleted
        return requests.put(
            f"{self.url}/api-v2/projects/{project_id}",
            json=payload,
            headers=self.headers
        )
