from src.utils.AssertionUtil import *
from src.utils.NumberUtil import *
from src.utils.RequestUtil import *
from src.utils.StringUtil import *

def Insert_Pet():
    """
    Inserting a Pet to get in below functions
    """
    url = get_URL("CREATE_PET_SERVICE")
    jsonbody = get_JsonData("PetsService.yml", "pet_service")
    jsonbody['name'] = generate_random_string_alphanumeric(6)
    jsonbody['id'] = get_random_number_between(1, 10)
    response = postRequest(url, json=jsonbody)
    response = eval(response.text)
    return response['id']

def Update_Pet_Status(id,status):
    """
    Updating a Pet Status to validate in below functions
    """
    url = get_URL("UPDATE_PET_SERVICE")
    jsonbody = get_JsonData("PetsService.yml", "pet_service")
    jsonbody['id'] = id
    jsonbody['status'] = status
    putRequest(url, json=jsonbody)

@allure.title("Update Pet Status And Validate By Get API")
def test_validate_updated_pet_status():
    id=Insert_Pet()
    Update_Pet_Status(id,"sold")
    url = get_URL("GET_PET_BY_STATUS_SERVICE")+("sold")
    responses = getRequest(url)
    responses = eval(responses.text)
    for response in responses :
            if(response['id'] == id):
                assert_equal(response['status'], "sold", "Pet status is not updated correctly.")

@allure.title("Get Pet By Invalid Status And Validate Status Code")
def test_get_pet_by_invalid_status():
    invalid_statuses = [generate_random_string_lowercase(4), generate_random_string_alphanumeric(4),
               generate_random_string_uppercase(4), str(get_random_number_between(1, 999))]
    for iv in invalid_statuses:
        url = get_URL("GET_PET_BY_STATUS_SERVICE")+iv
        getRequest(url,400)
