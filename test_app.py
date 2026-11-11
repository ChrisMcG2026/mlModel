import pytest
from flaskApp import app

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
    
def test_predict_salary_success(client):
    """Verify valid experience input returns a prediction string."""
    response = client.get("/predict?experience=5")
    body = response.data.decode("utf-8")

    assert response.status_code == 200
    assert body.startswith("The predicted value is")

