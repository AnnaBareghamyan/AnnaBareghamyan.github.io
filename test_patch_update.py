import requests
import pytest
import allure
from datetime import datetime


@allure.feature("API Tests")
@allure.story("Update User Data with PATCH")
@allure.title("Test PATCH Request to Update User")
@pytest.mark.smoke
def test_patch_user():
    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }

    with allure.step("Send PATCH request"):
        response = requests.patch("https://reqres.in/api/users/2", json=payload)

    with allure.step("Validate response status code"):
        assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

    with allure.step("Validate response body"):
        response_data = response.json()
        expected_keys = ["name", "job", "updatedAt"]

        for key in expected_keys:
            assert key in response_data, f"Response does not contain key: {key}"

        assert response_data["name"] == "morpheus", f"Expected name 'morpheus' but got {response_data['name']}"
        assert response_data["job"] == "zion resident", f"Expected job 'zion resident' but got {response_data['job']}"

        updated_at = response_data["updatedAt"]
        assert updated_at.startswith(
            datetime.now().isoformat().split("T")[0]), "updatedAt does not start with today's date"


if __name__ == "__main__":
    pytest.main()