import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

from utilities.properties.readProperties import ReadConfig


class Leaves:
    """ Reading Web Element Locators From Config File"""

    button_my_info = ReadConfig.get_button_my_info_xpath()
    button_personal_details = ReadConfig.get_button_personal_details_xpath()
    text_employee_first_name = ReadConfig.get_text_employee_first_name_xpath()

    def __init__(self, driver):
        self.driver = driver

    """This method is useful to perform click action on PIM button"""

    def click_my_info(self):
        self.driver.find_element(By.XPATH, self.button_my_info).click()
        time.sleep(2)
