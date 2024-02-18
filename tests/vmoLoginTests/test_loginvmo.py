import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.pageobjects.login_page1 import LoginPage
import allure
import os
from dotenv import load_dotenv

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    driver.maximize_window()
    return driver

@allure.feature("TC#1 - VMO App negative Test")
def test_login_negative(setup):

    driver = setup
    login_page = LoginPage(driver)
    login_page.login_to_vwo("test","ATBx@1234")
    time.sleep(5)
    error_message = login_page.error_message_text()
    assert error_message == "Your email, password, IP address or location did not match"
    time.sleep(3)

@allure.epic("VMO Login Test")
@allure.feature("TC#1 - VMO App positive Test")
def test_login(setup):

    driver = setup
    login_page = LoginPage(driver)
    login_page.login_to_vwo()
    time.sleep(5)
    assert "Dashboard" in driver.title
    time.sleep(3)
