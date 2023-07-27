import allure
import yaml
from src.utils.LoggerUtil import *

@allure.step("Get URL : {0}")
def get_URL(key):
    host=get_HOST("HOST")
    path=os.getcwd();
    url_path=path.split("src")
    url_path=url_path[0]+"/src/resources/url/url.yml"
    url=getValueFromFile(key, url_path)
    final_url=host+url
    return final_url

def getValueFromFile(key, path):
    try:
        with open(path, 'r') as ymlfile:
            config = yaml.load(ymlfile, Loader=yaml.FullLoader)
            ymlfile.close()
    except FileNotFoundError as e :
        log_error(path+" File Not Found "+e.strerror)
    else:
        log(config[key])
        return config[key]

@allure.step("Get Json Data From File : {0} For Key :{1}")
def get_JsonData(filename,key):
    path=os.getcwd()
    path=path.split("src")
    path=path[0]+"/src/resources/data/"+filename
    return getValueFromFile(key, path)

@allure.step("Get Value From Configuration For Key : {0}")
def get_valuefromConfig(key):
    path=os.getcwd()
    config_path=path.split("src")
    config_path=config_path[0]+"/src/config.yml"
    return getValueFromFile(key, config_path)

@allure.step("Get Value Of Host : {0}")
def get_HOST(key):
    return get_valuefromConfig(key)