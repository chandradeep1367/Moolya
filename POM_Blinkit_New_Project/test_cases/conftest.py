from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest
import os
from _datetime import datetime


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if not os.path.exists('reports'):
        os.makedirs('reports')
    config.option.htmlpath = f'reports/report_{datetime.now().strftime("%d-%m-%Y %H-%M-%S")}.html'


@pytest.fixture()
def _driver():
    obj_service = Service()
    driver = webdriver.Chrome(service=obj_service)
    driver.get('https://blinkit.com/')
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.close()