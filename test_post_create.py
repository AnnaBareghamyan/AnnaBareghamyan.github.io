# CREATE
import requests
import pytest
import allure
from datetime import datetime


@allure.feature("API Tests")
@allure.story("Create User")
@allure.title("Test POST Request to Create User")
@pytest.mark.regression
def test_create_user():
    base_url = "https://reqres.in/api/users"
    payload = {
        "name": "morpheus",
        "job": "leader"
    }

    with allure.step("Send POST request"):
        response = requests.post(base_url, json=payload)

    with allure.step("Validate response status code"):
        assert response.status_code == 201, f"Expected status code 201 but got {response.status_code}"

    with allure.step("Validate response body"):
        response_data = response.json()
        expected_response_keys = ["name", "job", "id", "createdAt"]

        for key in expected_response_keys:
            assert key in response_data, f"Response does not contain key: {key}"

        assert response_data["name"] == "morpheus", f"Expected name 'morpheus' but got {response_data['name']}"
        assert response_data["job"] == "leader", f"Expected job 'leader' but got {response_data['job']}"

        # Validate createdAt field
        created_at = response_data["createdAt"]
        assert created_at.startswith(
            datetime.now().isoformat().split("T")[0]), "createdAt does not start with today's date"


if __name__ == "__main__":
    pytest.main()