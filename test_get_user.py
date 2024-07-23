import requests
import pytest
import allure


# LIST USERS

@allure.feature("User API")
@allure.story("List users")
@pytest.mark.regression
class TestUserAPI:

    @allure.title("Test retrieval of users list")
    @allure.description("Verify the list of users from the API response.")
    def test_list_users(self):
        response = requests.get("https://reqres.in/api/users?page=2")

        with allure.step("Check response status code"):
            assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

        data = response.json()

        with allure.step("Verify pagination details"):
            assert data["page"] == 2, f"Expected page 2, but got {data['page']}"
            assert data["per_page"] == 6, f"Expected per_page 6, but got {data['per_page']}"
            assert data["total"] == 12, f"Expected total 12, but got {data['total']}"
            assert data["total_pages"] == 2, f"Expected total_pages 2, but got {data['total_pages']}"

        expected_users = [
            {
                "id": 7,
                "email": "michael.lawson@reqres.in",
                "first_name": "Michael",
                "last_name": "Lawson",
                "avatar": "https://reqres.in/img/faces/7-image.jpg"
            },
            {
                "id": 8,
                "email": "lindsay.ferguson@reqres.in",
                "first_name": "Lindsay",
                "last_name": "Ferguson",
                "avatar": "https://reqres.in/img/faces/8-image.jpg"
            },
            {
                "id": 9,
                "email": "tobias.funke@reqres.in",
                "first_name": "Tobias",
                "last_name": "Funke",
                "avatar": "https://reqres.in/img/faces/9-image.jpg"
            },
            {
                "id": 10,
                "email": "byron.fields@reqres.in",
                "first_name": "Byron",
                "last_name": "Fields",
                "avatar": "https://reqres.in/img/faces/10-image.jpg"
            },
            {
                "id": 11,
                "email": "george.edwards@reqres.in",
                "first_name": "George",
                "last_name": "Edwards",
                "avatar": "https://reqres.in/img/faces/11-image.jpg"
            },
            {
                "id": 12,
                "email": "rachel.howell@reqres.in",
                "first_name": "Rachel",
                "last_name": "Howell",
                "avatar": "https://reqres.in/img/faces/12-image.jpg"
            }
        ]

        with allure.step("Verify user data"):
            for expected_user, actual_user in zip(expected_users, data["data"]):
                assert expected_user["id"] == actual_user[
                    "id"], f"Expected user ID {expected_user['id']}, but got {actual_user['id']}"
                assert expected_user["email"] == actual_user[
                    "email"], f"Expected email {expected_user['email']}, but got {actual_user['email']}"
                assert expected_user["first_name"] == actual_user[
                    "first_name"], f"Expected first name {expected_user['first_name']}, but got {actual_user['first_name']}"
                assert expected_user["last_name"] == actual_user[
                    "last_name"], f"Expected last name {expected_user['last_name']}, but got {actual_user['last_name']}"
                assert expected_user["avatar"] == actual_user[
                    "avatar"], f"Expected avatar URL {expected_user['avatar']}, but got {actual_user['avatar']}"

        # Assert support info
        with allure.step("Verify support information"):
            assert data["support"][
                       "url"] == "https://reqres.in/#support-heading", f"Expected support URL, but got {data['support']['url']}"
            assert data["support"][
                       "text"] == "To keep ReqRes free, contributions towards server costs are appreciated!", \
                f"Expected support text, but got {data['support']['text']}"


# SINGLE USER

@allure.feature("User API")
@allure.story("Get Single User")
@allure.title("Fetch Single User by ID")
@pytest.mark.parametrize("expected_status_code, expected_user_data", [
    (200, {
        "id": 2,
        "email": "janet.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver",
        "avatar": "https://reqres.in/img/faces/2-image.jpg"
    })
])
def test_get_single_user(expected_status_code, expected_user_data):
    with allure.step("Send GET request to fetch user"):
        response = requests.get("https://reqres.in/api/users/2")

    with allure.step("Validate response status code"):
        assert response.status_code == expected_status_code

    with allure.step("Validate response data"):
        response_data = response.json().get("data")
        assert response_data == expected_user_data


# SINGLE USER NOT FOUND
@allure.feature("API Tests")
@allure.story("Get Non-Existent User Data")
@allure.title("Test GET Request for Non-Existent User")
def test_get_non_existent_user():

    with allure.step("Send GET request"):
        response = requests.get("https://reqres.in/api/users/23")

    with allure.step("Validate response status code"):
        assert response.status_code == 404, f"Expected status code 404 but got {response.status_code}"

    with allure.step("Validate response body"):
        # Adjusted to check for an empty response instead
        expected_response = {}
        assert response.json() == expected_response, f"Expected response {expected_response} but got {response.json()}"


if __name__ == "__main__":
    pytest.main()