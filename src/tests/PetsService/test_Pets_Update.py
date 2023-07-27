from src.utils.AssertionUtil import *
from src.utils.NumberUtil import *
from src.utils.RequestUtil import *
from src.utils.StringUtil import *

def Insert_Pet():
    """
    Inserting a Pet to edit in below functions
    """
    url = get_URL("CREATE_PET_SERVICE")
    jsonbody = get_JsonData("PetsService.yml", "pet_service")
    jsonbody['name'] = generate_random_string_alphanumeric(6)
    jsonbody['id'] = get_random_number_between(1, 10)
    response = postRequest(url, json=jsonbody)
    response = eval(response.text)
    return response['id']

@allure.title("Validate API Response For Update Pet Status Request")
def test_update_pet_status():
    id=Insert_Pet()
    url = get_URL("UPDATE_PET_SERVICE")
    jsonbody = get_JsonData("PetsService.yml", "pet_service")
    statuses = ["available","pending","sold"]
    jsonbody['id'] = id
    for status in statuses:
        jsonbody['status'] = status
        putRequest(url,jsonbody)

@allure.title("Validate API Response For Update Photo URLs)")
def test_update_pet_photo_url():
    id=Insert_Pet()
    url = get_URL("UPDATE_PET_SERVICE")
    jsonbody = get_JsonData("PetsService.yml", "pet_service")
    URLs= ["http://sampleurl.com","http://sampleurl2.com"]
    jsonbody['id'] = id
    jsonbody['photoUrls'] = URLs
    putRequest(url,jsonbody)

@allure.title("Validate API response for incorrect uri in update pet request")
def test_update_pet_invalid_uri():
    id = Insert_Pet()
    url = get_URL("UPDATE_PET_SERVICE")
    invalid = [generate_random_string_lowercase(4), generate_random_string_alphanumeric(4),
               generate_random_string_uppercase(4), str(get_random_number_between(1, 999))]
    jsonbody = get_JsonData("PetsService.yml", "pet_service")
    jsonbody['id']=id
    for iv in invalid:
        url = url + str(iv)
        putRequest(url, json=jsonbody, statuscode=405)