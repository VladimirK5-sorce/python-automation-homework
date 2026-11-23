import os
import uuid
import pytest
from lesson_08.Projects_api import ProjectsApi


BASE_URL = "https://yougile.com"
TOKEN = os.getenv("YOUGILE_TOKEN", "YOUR_TOKEN_HERE")


@pytest.fixture
def api():
    return ProjectsApi(BASE_URL, TOKEN)


@pytest.fixture
def created_project_id(api):
    title = f"Test Project {uuid.uuid4()}"
    resp = api.create_project(title=title)
    assert resp.status_code == 201
    project_id = resp.json()["id"]
    yield project_id
    api.update_project(project_id=project_id, deleted=True)


# --- [POST] /api-v2/projects ---

def test_create_project_positive(api):
    title = f"New Project {uuid.uuid4()}"
    resp = api.create_project(title=title)
    assert resp.status_code == 201
    data = resp.json()
    assert "id" in data
    api.update_project(project_id=data["id"], deleted=True)


def test_create_project_negative_empty_title(api):
    resp = api.create_project(title="")
    assert resp.status_code == 400


# --- [GET] /api-v2/projects/{id} ---

def test_get_project_positive(api, created_project_id):
    resp = api.get_project(project_id=created_project_id)
    assert resp.status_code == 200
    assert resp.json()["id"] == created_project_id


def test_get_project_negative_not_found(api):
    fake_id = str(uuid.uuid4())
    resp = api.get_project(project_id=fake_id)
    assert resp.status_code == 404


# --- [PUT] /api-v2/projects/{id} ---

def test_update_project_positive(api, created_project_id):
    new_title = f"Updated Project {uuid.uuid4()}"
    resp = api.update_project(project_id=created_project_id, title=new_title)
    assert resp.status_code == 200
    assert resp.json()["id"] == created_project_id

    get_resp = api.get_project(project_id=created_project_id)
    assert get_resp.json()["title"] == new_title


def test_update_project_negative_not_found(api):
    fake_id = str(uuid.uuid4())
    resp = api.update_project(project_id=fake_id, title="Updated Title")
    assert resp.status_code == 404
