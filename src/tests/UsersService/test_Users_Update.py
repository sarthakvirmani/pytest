from src.utils.NumberUtil import *
from src.utils.RequestUtil import *
from src.utils.StringUtil import *

def Insert_User():
    """
    Inserting a User to edit in below functions
    """
    users = []
    url = get_URL("CREATE_USER_WITH_ARRAY_SERVICE")
    jsonbody = get_JsonData("UsersService.yml", "user_service")
    jsonbody['id'] = get_random_number_between(1,10)
    jsonbody['username'] = generate_random_string_lowercase(5)
    users.append(jsonbody)
    response = postRequest(url, json=users)
    response = eval(response.text)
    return jsonbody['username']

@allure.title("Validate API Response For Update Username")
def test_update_username():
    username=Insert_User()
    url = get_URL("UPDATE_USER_SERVICE")+username
    jsonbody = get_JsonData("UsersService.yml", "user_service")
    updated_username=generate_random_string_lowercase(10)
    jsonbody['username'] = updated_username
    putRequest(url,jsonbody)

@allure.title("Validate API Response For Updating First And Last Name)")
def test_update_first_and_lastname():
    username=Insert_User()
    url = get_URL("UPDATE_USER_SERVICE")+username
    jsonbody = get_JsonData("UsersService.yml", "user_service")
    updated_first_name = generate_random_string_lowercase(5)
    updated_last_name = generate_random_string_lowercase(5)
    jsonbody['firstName'] = updated_first_name
    jsonbody['lastName'] = updated_last_name
    putRequest(url,jsonbody)

@allure.title("Validate API Response For Update User With Invalid HTTP Method")
def test_update_user_invalid_http_method():
    url = get_URL("UPDATE_USER_SERVICE")
    getRequest(url,statuscode=405)