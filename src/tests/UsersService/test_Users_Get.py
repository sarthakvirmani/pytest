from src.utils.NumberUtil import *
from src.utils.RequestUtil import *
from src.utils.StringUtil import *
from src.utils.AssertionUtil import *

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

def Update_User_Username(username,updated_username):
    """
    Updating User's Username to validate in below functions
    """
    url = get_URL("UPDATE_USER_SERVICE") + username
    jsonbody = get_JsonData("UsersService.yml", "user_service")
    jsonbody['username'] = updated_username
    putRequest(url, jsonbody)

@allure.title("Update User's Username And Validate By Get API")
def test_validate_updated_username():
    username=Insert_User()
    updated_username = generate_random_string_lowercase(5)
    Update_User_Username(username,updated_username)
    url = get_URL("GET_USER_SERVICE")+updated_username
    response = getRequest(url)
    response = eval(response.text)
    assert_equal(response['username'],updated_username,"User Name is not updated correctly.")

@allure.title("Get User By Invalid Username And Validate Status Code")
def test_get_user_by_invalid_username():
    url = get_URL("GET_USER_SERVICE")+generate_random_string_lowercase(5)
    response = getRequest(url,404)
    response = eval(response.text)
    assert_equal(response['message'],"User not found","Error message is incorrect for invalid username.")