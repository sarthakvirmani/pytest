# This class contains method to make api calls .

import requests
from src.utils.FileUtil import *
import json
from src.utils.LoggerUtil import *


HOST = get_valuefromConfig("HOST")

@allure.step("GET Request For URL : {0}")
def getRequest(url, statuscode=200):
    """Sends a GET request.

    :param url: URL for the new :class:`Request` object.
    :param params: (optional) Dictionary, list of tuples or bytes to send
        in the query string for the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """
    response = requests.get(url)
    log("Response: "+response.text)
    assert statuscode == response.status_code, "Status Code "+str(statuscode) +" Expected ,Found Status Code :"+str(response.status_code)
    return response

@allure.step("DELETE Request For URL : {0}")
def deleteRequest(url, statuscode=200):
    r"""Sends a DELETE request.

    :param url: URL for the new :class:`Request` object.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """
    response = requests.delete(url)
    log("Response: "+response.text)
    assert statuscode == response.status_code, "Status Code "+str(statuscode) +" Expected ,Found Status Code :"+str(response.status_code)
    return response

@allure.step("PUT Request For URL : {0}")
def putRequest(url, json=None, statuscode=200):
    r"""Sends a PUT request.

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body of the :class:`Request`.
    :param json: (optional) json data to send in the body of the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """
    response = requests.put(url, json=json)
    log("Response: "+response.text)
    assert statuscode == response.status_code, "Status Code "+str(statuscode) +" Expected , Found Status Code :"+str(response.status_code)
    return response

@allure.step("POST Request For URL : {0}")
def postRequest(url, json=None, statuscode=200):
    r"""Sends a POST request.

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body of the :class:`Request`.
    :param json: (optional) json data to send in the body of the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """
    response = requests.post(url, json=json)
    log("Response: "+response.text)
    assert statuscode == response.status_code, "Status Code "+str(statuscode) +" Expected , Found Status Code :"+str(response.status_code)
    return response

