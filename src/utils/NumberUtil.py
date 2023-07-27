# This class contains method on Numbers
import random
from src.utils.LoggerUtil import *

@allure.step("Generate Random Number Between {0} and {1}")
def get_random_number_between(start,end):
    """
    This method generate Random Number Between start and end.
    :param start: Start value
    :param end: end value
    :return: Return random number
    """
    number=random.randrange(start,end)
    log_info('Random Number Generated : '+str(number))
    # log('Random Number Generated : '+str(number))
    return number

@allure.step("Generate Random Integer Number")
def get_random_integer_number():
    """
    This method generate random integer number
    :return: Random number
    """
    number=random.randint()
    log('Random Number Generated : '+str(number))
    return number


def get_random_choice(value):
    """
    This method would return random from given argument
    :param value: list / string of value
    :return: random number from value
    """
    number=random.choice(value)
    log('Random Value Generated : '+str(number))
    return number

def get_random_float_between(start,end):
    """
    This method generate Random float Number Between start and end.
    :param start: Start value
    :param end: end value
    :return: Return float number
    """
    number=random.uniform(start,end)
    print('Random Number Generated Is : '+str(number))
    return number
