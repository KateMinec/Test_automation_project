import pytest
import requests

BASE_URL = "https://typicode.com"


@pytest.fixture(scope="session")
def api_session():
    """Создает единую HTTP-сессию для всех API-тестов."""
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json; charset=UTF-8"})
    yield session
    session.close()


@pytest.mark.parametrize("post_id, expected_user_id", [
    (1, 1),
    (15, 2),
    (50, 5),
])
def test_get_post_by_id(api_session, post_id, expected_user_id):
    """Проверка получения существующего поста по ID (GET)."""
    response = api_session.get(f"{BASE_URL}/posts/{post_id}")

    assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"

    body = response.json()
    assert body["id"] == post_id
    assert body["userId"] == expected_user_id
    assert isinstance(body["title"], str) and len(body["title"]) > 0
    assert isinstance(body["body"], str)


def test_create_post(api_session):
    """Проверка создания нового ресурса (POST)."""
    payload = {
        "title": "Avito QA Internship Test",
        "body": "Testing REST API with Pytest and Requests",
        "userId": 101
    }

    response = api_session.post(f"{BASE_URL}/posts", json=payload)

    assert response.status_code == 201, f"Ожидался статус 201, получен {response.status_code}"

    body = response.json()
    assert body["title"] == payload["title"]
    assert body["body"] == payload["body"]
    assert body["userId"] == payload["userId"]
    assert "id" in body


def test_update_post(api_session):
    """Проверка полного обновления ресурса (PUT)."""
    post_id = 1
    updated_payload = {
        "id": post_id,
        "title": "Updated Title",
        "body": "Updated Body",
        "userId": 1
    }

    response = api_session.put(f"{BASE_URL}/posts/{post_id}", json=updated_payload)

    assert response.status_code == 200
    body = response.json()
    assert body["title"] == "Updated Title"
    assert body["body"] == "Updated Body"


def test_delete_post(api_session):
    """Проверка удаления ресурса (DELETE)."""
    response = api_session.delete(f"{BASE_URL}/posts/1")

    assert response.status_code == 200
    assert response.json() == {}


def test_get_nonexistent_post_returns_404(api_session):
    """Негативный тест: запрос несуществующего поста возвращает 404."""
    response = api_session.get(f"{BASE_URL}/posts/999999")

    assert response.status_code == 404
    assert response.json() == {}
