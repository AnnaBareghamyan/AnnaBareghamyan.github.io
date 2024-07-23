import requests
import pytest
import allure

# POST REGISTER SUCCESSFUL

@allure.feature("API Tests")
@allure.story("User Login")
@allure.title("Test POST Request for User Login")
@pytest.mark.regression
def test_login():

    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }

    with allure.step("Send POST request for login"):
        response = requests.post("https://reqres.in/api/login", json=payload)

    with allure.step("Validate response status code"):
        assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

    with allure.step("Validate response body"):
        response_data = response.json()
        assert "token" in response_data, "Response does not contain a token"


if __name__ == "__main__":
    pytest.main()


# POST REGISTER UNSUCCESSFUL
@allure.feature("API Tests")
@allure.story("User Registration")
@allure.title("Test POST Request for User Registration with Missing Password")
def test_register_missing_password():
    payload = {
        "email": "sydney@fife"
    }

    with allure.step("Send POST request for registration without password"):
        response = requests.post("https://reqres.in/api/register", json=payload)

    with allure.step("Validate response status code"):
        assert response.status_code == 400, f"Expected status code 400 but got {response.status_code}"

    with allure.step("Validate response body"):
        response_data = response.json()
        expected_error = {"error": "Missing password"}
        assert response_data == expected_error, f"Expected response {expected_error} but got {response_data}"


if __name__ == "__main__":
    pytest.main()