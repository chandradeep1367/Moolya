import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# @pytest.mark.usefixtures("setup")
# class BaseTest:
#     pass

@pytest.fixture(scope="class", params=["chrome"])
def setup(request):
    global driver
    if request.param == "chrome":
        service_obj = Service()
        driver = webdriver.Chrome(service=service_obj)
    request.cls.driver = driver
    try:
        driver.get("https://blinkit.com/")
        time.sleep(5)
        driver.find_element(By.XPATH, "//button[text()='Detect my location']").click()
        time.sleep(10)
    except:
        print("NO POPup")
    # if request.param =="firefox":
    #     service_obj = Service()
    #     driver = webdriver.Firefox(service=service_obj)

    driver.maximize_window()
    time.sleep(5)

    yield driver
    driver.close()


    # global driver
    # service_obj = Service()
    # driver = webdriver.Chrome(service=service_obj)
    # driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    # yield driver
    # driver.close()
