import requests
import pytest
import allure


@allure.feature("API Tests")
@allure.story("Get Users List")
@allure.title("Test GET Request to Retrieve Users List")
@pytest.mark.regression
def test_get_users():
    base_url = "https://reqres.in/api/users?delay=3"

    with allure.step("Send GET request to fetch users"):
        response = requests.get(base_url)

    with allure.step("Validate response status code"):
        assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

    with allure.step("Validate response body"):
        response_data = response.json()
        expected_keys = ["page", "per_page", "total", "total_pages", "data", "support"]

        for key in expected_keys:
            assert key in response_data, f"Response does not contain key: {key}"

        # Validate structure of data
        assert isinstance(response_data["data"], list), "Expected 'data' to be a list"
        assert len(response_data["data"]) == 6, f"Expected 6 users but got {len(response_data['data'])}"

        # Validate each user data structure
        for user in response_data["data"]:
            assert "id" in user
            assert "email" in user
            assert "first_name" in user
            assert "last_name" in user
            assert "avatar" in user


if __name__ == "__main__":
    pytest.main()