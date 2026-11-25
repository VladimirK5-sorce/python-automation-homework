import os
import pytest
from dotenv import load_dotenv
from lesson_09.subjects_table import SubjectsTable

load_dotenv()

DB_URL = os.getenv("DB_CONNECTION_STRING")


@pytest.fixture(scope="module")
def db():
    assert DB_URL, "Не задана переменная DB_CONNECTION_STRING в файле .env"
    return SubjectsTable(DB_URL)


@pytest.fixture
def created_subject(db):
    new_id = db.get_max_id() + 1
    title = f"Test Subject {new_id}"
    db.create(new_id, title)
    yield {"id": new_id, "title": title}
    db.delete(new_id)


def test_add_subject(db):
    new_id = db.get_max_id() + 1
    title = f"AutoTest Subject {new_id}"

    db.create(new_id, title)
    row = db.get_by_id(new_id)

    try:
        assert row is not None
        assert row["subject_id"] == new_id
        assert row["subject_title"] == title
    finally:
        db.delete(new_id)


def test_update_subject(db, created_subject):
    subject_id = created_subject["id"]
    updated_title = f"Updated Subject {subject_id}"

    db.update(subject_id, updated_title)
    row = db.get_by_id(subject_id)

    assert row is not None
    assert row["subject_title"] == updated_title


def test_delete_subject(db):
    new_id = db.get_max_id() + 1
    db.create(new_id, f"To Delete {new_id}")

    db.delete(new_id)
    row = db.get_by_id(new_id)

    assert row is None
