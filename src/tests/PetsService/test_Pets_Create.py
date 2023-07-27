from src.utils.AssertionUtil import *
from src.utils.NumberUtil import *
from src.utils.RequestUtil import *
from src.utils.StringUtil import *


@allure.title("Validate API Response For Create Pet Request")
def test_createPet():
    url = get_URL("CREATE_PET_SERVICE")
    jsonbody = get_JsonData("PetsService.yml", "pet_service")
    jsonbody['name'] = generate_random_string_alphanumeric(6)
    jsonbody['id'] = get_random_number_between(1,10)
    print(jsonbody)
    response = postRequest(url, json=jsonbody)
    response = eval(response.text)
    assert_equal(jsonbody,response,"Created and Provided JSONs are not same")

@allure.title("Validate API response for incorrect uri in create pet request")
def test_createPet_Invalid_URI():
    url = get_URL("CREATE_PET_SERVICE")
    invalid = [generate_random_string_lowercase(4), generate_random_string_alphanumeric(4),
               generate_random_string_uppercase(4), str(get_random_number_between(1, 999))]
    for iv in invalid:
        url = url + str(iv)
        jsonbody = get_JsonData("PetsService.yml", "pet_service")
        postRequest(url, json=jsonbody, statuscode=404)

@allure.title("Validate API response for invalid HTTP Method")
def test_createPet_Invalid_HTTP_Method():
    url = get_URL("CREATE_PET_SERVICE")
    response=getRequest(url,statuscode=405)

@allure.title("Validate API response for invalid Pet Name")
def test_createPet_Invalid_Name():
    url = get_URL("CREATE_PET_SERVICE")
    jsonbody = get_JsonData("PetsService.yml", "pet_service")
    jsonbody['id'] = generate_random_string_alphanumeric(6)
    response=postRequest(url, json=jsonbody, statuscode=500)
