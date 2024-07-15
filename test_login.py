
import requests
import pytest
import allure

# LOGIN SUCCESSFULL
@allure.feature("API Tests")
@allure.story("User Login")
@allure.title("Test POST Request for Successful User Login")
def test_login_success():
    base_url = "https://reqres.in/api/login"
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    with allure.step("Send POST request for login"):
        response = requests.post(base_url, json=payload)

    with allure.step("Validate response status code"):
        assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

    with allure.step("Validate response body"):
        response_data = response.json()
        expected_token = {"token": "QpwL5tke4Pnpja7X4"}
        assert response_data == expected_token, f"Expected response {expected_token} but got {response_data}"


if __name__ == "__main__":
    pytest.main()

# LOGIN UNSUCCESSFULL

@allure.feature("API Tests")
@allure.story("User Login")
@allure.title("Test POST Request for Login with Missing Password")
def test_login_missing_password():
    base_url = "https://reqres.in/api/login"
    payload = {
        "email": "peter@klaven"
    }

    with allure.step("Send POST request for login without password"):
        response = requests.post(base_url, json=payload)

    with allure.step("Validate response status code"):
        assert response.status_code == 400, f"Expected status code 400 but got {response.status_code}"

    with allure.step("Validate response body"):
        response_data = response.json()
        expected_error = {"error": "Missing password"}
        assert response_data == expected_error, f"Expected response {expected_error} but got {response_data}"


if __name__ == "__main__":
    pytest.main()
