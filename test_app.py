import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_welcome_route(client):
    """Verify the root endpoint returns the expected greeting."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Welcome Everyone"

