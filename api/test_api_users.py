import requests
import pytest
from config.api_config import BASE_URL, HEADERS

def test_get_users_list():
    """Tests that we can retrieve a list of users."""
    response = requests.get(f"{BASE_URL}/users?page=2")
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    json_response = response.json()
    assert "page" in json_response
    assert "data" in json_response
    assert isinstance(json_response["data"], list)
    assert len(json_response["data"]) > 0, "User data list is empty"

def test_create_user():
    """Tests that we can create a new user using the authorized API key."""
    payload = {
        "name": "morpheus",
        "job": "leader"
    }

    response = requests.post(f"{BASE_URL}/users", json=payload, headers=HEADERS)

    # Assert status code
    assert response.status_code == 201, f"Expected status code 201 but got {response.status_code}"

    # Assert response content
    json_response = response.json()
    assert json_response["name"] == payload["name"]
    assert json_response["job"] == payload["job"]
    assert "id" in json_response
    assert "createdAt" in json_response
