import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(params=["chrome"], scope='class')
def init_Driver(request):
    global driver
    if request.param == "chrome":
        service = Service()
        driver = webdriver.Chrome(service=service)
    request.cls.driver = driver
    driver.maximize_window()
    try:
        driver.find_element(By.XPATH, "//button[text()='Detect my location']").click()
        time.sleep(10)
    except:
        print("NO POPup")

    yield driver
    time.sleep(5)
    driver.close()
