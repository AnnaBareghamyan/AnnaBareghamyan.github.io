import requests
import pytest
import allure


@allure.feature("API Tests")
@allure.story("Delete User Data")
@allure.title("Test DELETE Request to Remove User")
@pytest.mark.regression
def test_delete_user():
    base_url = "https://reqres.in/api/users/2"

    with allure.step("Send DELETE request"):
        response = requests.delete(base_url)

    with allure.step("Validate response status code"):
        assert response.status_code == 204, f"Expected status code 204 but got {response.status_code}"

    with allure.step("Validate response body"):
        assert response.text == "", "Expected response body to be empty for status 204"


if __name__ == "__main__":
    pytest.main()