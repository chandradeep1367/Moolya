from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest


@pytest.fixture()
def _driver():
    obj_service = Service()
    driver = webdriver.Chrome(service=obj_service)
    driver.get('https://blinkit.com/')
    driver.maximize_window()
    yield driver
    driver.close()