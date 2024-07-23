import requests
import pytest
import allure

# LIST <RESOURCE>

@allure.feature("API Tests")
@allure.story("Get Unknown Color Data")
@allure.title("Test Get Request for Colors")
@pytest.mark.smoke
def test_get_colors():

    with allure.step("Send GET request"):
        response = requests.get("https://reqres.in/api/unknown")

    with allure.step("Validate response status code"):
        assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

    with allure.step("Validate response body"):
        expected_response = {
            "page": 1,
            "per_page": 6,
            "total": 12,
            "total_pages": 2,
            "data": [
                {
                    "id": 1,
                    "name": "cerulean",
                    "year": 2000,
                    "color": "#98B2D1",
                    "pantone_value": "15-4020"
                },
                {
                    "id": 2,
                    "name": "fuchsia rose",
                    "year": 2001,
                    "color": "#C74375",
                    "pantone_value": "17-2031"
                },
                {
                    "id": 3,
                    "name": "true red",
                    "year": 2002,
                    "color": "#BF1932",
                    "pantone_value": "19-1664"
                },
                {
                    "id": 4,
                    "name": "aqua sky",
                    "year": 2003,
                    "color": "#7BC4C4",
                    "pantone_value": "14-4811"
                },
                {
                    "id": 5,
                    "name": "tigerlily",
                    "year": 2004,
                    "color": "#E2583E",
                    "pantone_value": "17-1456"
                },
                {
                    "id": 6,
                    "name": "blue turquoise",
                    "year": 2005,
                    "color": "#53B0AE",
                    "pantone_value": "15-5217"
                }
            ],
            "support": {
                "url": "https://reqres.in/#support-heading",
                "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
            }
        }
        assert response.json() == expected_response, f"Expected response does not match: {response.json()}"


if __name__ == "__main__":
    pytest.main()


# SINGLE <RESOURCE>
@allure.feature("API Tests")
@allure.story("Get Single Unknown Color Data")
@allure.title("Test Get Request for Single Color")
def test_get_single_color():

    with allure.step("Send GET request"):
        response = requests.get("https://reqres.in/api/unknown/2")

    with allure.step("Validate response status code"):
        assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

    with allure.step("Validate response body"):
        expected_response = {
            "data": {
                "id": 2,
                "name": "fuchsia rose",
                "year": 2001,
                "color": "#C74375",
                "pantone_value": "17-2031"
            },
            "support": {
                "url": "https://reqres.in/#support-heading",
                "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
            }
        }
        assert response.json() == expected_response, f"Expected response does not match: {response.json()}"


if __name__ == "__main__":
    pytest.main()


# SINGLE <RESOURCE> NOT FOUND
@allure.feature("API Tests")
@allure.story("Get Non-Existent Resource Data")
@allure.title("Test GET Request for Non-Existent Resource")
def test_get_non_existent_resource():

    with allure.step("Send GET request"):
        response = requests.get("https://reqres.in/api/unknown/23")

    with allure.step("Validate response status code"):
        assert response.status_code == 404, f"Expected status code 404 but got {response.status_code}"

    with allure.step("Validate response body"):
        expected_response = {}
        assert response.json() == expected_response, f"Expected response {expected_response} but got {response.json()}"


if __name__ == "__main__":
    pytest.main()
