import logging
import allure
import os
path=os.getcwd().split("src")

logging.basicConfig(filename=path[0]+"logfile.log",format='%(asctime)s - %(message)s',level=logging.INFO)

@allure.step("Log.Info : {0}")
def log_info(message):
    logging.info(message)
    print(message)

@allure.step("Log.Info : {0}")
def log_error(message):
    logging.info(message)
    print(message)

def log(message):
    log_info(message)
    print(message)
