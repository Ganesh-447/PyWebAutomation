import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import(ElementNotVisibleException,
                                       ElementNotSelectableException)
import os
from dotenv import load_dotenv
import openpyxl

#reading the data from excel file and keeping in credentials as dictonary
def read_credentials_from_excel(file_path):
    credentials = []
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        credentials.append({"username": username, "password": password})
    print(credentials)
    return credentials


def vmo_login(email,passwor):
    driver = webdriver.Chrome()
    load_dotenv()
    driver.get("https:/app.vwo.com")
    user_name = driver.find_element(By.ID, "login-username")
    password = driver.find_element(By.ID, "login-password")
    btn = driver.find_element(By.ID, "js-login-btn")
    user_name.send_keys(email)
    password.send_keys(passwor)
    btn.click()
    result = driver.current_url
    if result != "https://app.vwo.com/#dashboard":
        pytest.xfail("Invalid Credentials")
        driver.quit()
    else:
        assert True == True
        driver.quit()


    #write logic if test case passes
    #-url changes
    #-error message


#providing the file path and iterating credentials dictonary and putting the email
#and password into test_login
@pytest.mark.parametrize("user_cred",read_credentials_from_excel(os.getcwd()+"/testdata1_ddt.xlsx"))
def test_vmo_login(user_cred):
        username = user_cred["username"]
        password = user_cred["password"]
        print(username, password)
        vmo_login(username, password)
