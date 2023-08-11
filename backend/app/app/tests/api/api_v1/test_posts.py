from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.post import create_random_post


def test_create_post(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    data = {"title": "Foo", "description": "Fighters"}
    response = client.post(
        f"{settings.API_V1_STR}/posts/", headers=superuser_token_headers, json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == data["title"]
    assert content["description"] == data["description"]
    assert "id" in content
    assert "owner_id" in content


def test_read_post(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    post = create_random_post(db)
    response = client.get(
        f"{settings.API_V1_STR}/posts/{post.id}", headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == post.title
    assert content["description"] == post.description
    assert content["id"] == post.id
    assert content["owner_id"] == post.owner_id
