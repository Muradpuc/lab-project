from fastapi.testclient import TestClient
from src.main import app


client = TestClient(app)


def test_get_all_students():
    response = client.get("/students")

    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_get_single_student():
    response = client.get("/students/1")

    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_get_nonexistent_student():
    response = client.get("/students/999")

    assert response.status_code == 404


def test_create_student():
    new_student = {
        "id": 10,
        "name": "Rahim Ahmed",
        "department": "CSE",
        "semester": 4,
        "cgpa": 3.80
    }

    response = client.post(
        "/students",
        json=new_student
    )

    assert response.status_code == 201
    assert response.json()["name"] == "Rahim Ahmed"


def test_create_duplicate_student():
    new_student = {
        "id": 1,
        "name": "Another Student",
        "department": "CSE",
        "semester": 4,
        "cgpa": 3.20
    }

    response = client.post(
        "/students",
        json=new_student
    )

    assert response.status_code == 400


def test_update_student():
    updated_student = {
        "id": 1,
        "name": "Murad Hasan Updated",
        "department": "CSE",
        "semester": 5,
        "cgpa": 3.80
    }

    response = client.put(
        "/students/1",
        json=updated_student
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Murad Hasan Updated"


def test_update_nonexistent_student():
    updated_student = {
        "id": 999,
        "name": "Unknown Student",
        "department": "CSE",
        "semester": 4,
        "cgpa": 3.00
    }

    response = client.put(
        "/students/999",
        json=updated_student
    )

    assert response.status_code == 404


def test_delete_student():
    response = client.delete("/students/2")

    assert response.status_code == 200
    assert response.json()["message"] == "Student deleted successfully"


def test_delete_nonexistent_student():
    response = client.delete("/students/999")

    assert response.status_code == 404