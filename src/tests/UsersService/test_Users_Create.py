from src.utils.NumberUtil import *
from src.utils.RequestUtil import *
from src.utils.StringUtil import *


@allure.title("Validate API Response For Create Multiple Users Request")
def test_create_multiple_users():
    users = []
    url = get_URL("CREATE_USER_WITH_ARRAY_SERVICE")
    jsonbody = get_JsonData("UsersService.yml", "user_service")
    user_details=[{"id":get_random_number_between(1,10),"username":generate_random_string_lowercase(5)},
                  {"id":get_random_number_between(11,20),"username":generate_random_string_uppercase(5)}]
    for ud in user_details:
        jsonbody['id'] = ud['id']
        jsonbody['username'] = ud['username']
        users.append(jsonbody)
    log(users)
    postRequest(url, json=users)

@allure.title("Validate API Response For Create User With Invalid ID")
## Asserting the status code with 500 as API is giving 500 for invalid requests.
def test_create_user_with_invalid_id():
    users = []
    url = get_URL("CREATE_USER_WITH_ARRAY_SERVICE")
    jsonbody = get_JsonData("UsersService.yml", "user_service")
    jsonbody['id'] = generate_random_string_alphanumeric(5)
    jsonbody['username'] = generate_random_string_lowercase(5)
    users.append(jsonbody)
    log(users)
    postRequest(url, json=users, statuscode=500)

@allure.title("Validate API Response For Create User With Invalid HTTP Method")
def test_create_user_invalid_http_method():
    url = get_URL("CREATE_USER_WITH_ARRAY_SERVICE")
    getRequest(url,statuscode=405)

@allure.title("Validate API response for incorrect uri in create users request")
## Asserting the status code with 405 as API is giving 405 for invalid URIs.
def test_create_user_invalid_uri():
    url = get_URL("CREATE_USER_WITH_ARRAY_SERVICE")
    invalid = [generate_random_string_lowercase(4), generate_random_string_alphanumeric(4),
               generate_random_string_uppercase(4), str(get_random_number_between(1, 999))]
    for iv in invalid:
        url = url + str(iv)
        jsonbody = get_JsonData("UsersService.yml", "user_service")
        postRequest(url, json=jsonbody, statuscode=405)