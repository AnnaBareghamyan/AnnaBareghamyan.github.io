import requests
import pytest
import allure
from datetime import datetime


@allure.feature("API Tests")
@allure.story("Update User Data")
@allure.title("Test PUT Request to Update User")
@pytest.mark.regression
def test_update_user():
    base_url = "https://reqres.in/api/users/2"
    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }

    with allure.step("Send PUT request"):
        response = requests.put(base_url, json=payload)

    with allure.step("Validate response status code"):
        assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

    with allure.step("Validate response body"):
        response_data = response.json()
        expected_keys = ["name", "job", "updatedAt"]

        for key in expected_keys:
            assert key in response_data, f"Response does not contain key: {key}"

        assert response_data["name"] == "morpheus", f"Expected name 'morpheus' but got {response_data['name']}"
        assert response_data["job"] == "zion resident", f"Expected job 'zion resident' but got {response_data['job']}"


if __name__ == "__main__":
    pytest.main()