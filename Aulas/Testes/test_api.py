from api import app
import pytest

@pytest.fixture()
def client():
    app.config["TESTING"] = True
    return app.test_client()

def test_request_example(client):
    response = client.get("/")
    assert "ola" in response.text