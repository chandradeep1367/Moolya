import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

from utilities.properties.readProperties import ReadConfig


class Search_Customer_PIM:
    """ Reading Web Element Locators From Config File"""

    button_PIM = ReadConfig.get_button_PIM_xpath()
    button_employee_list = ReadConfig.get_button_employee_list_xpath()

    """This method is useful to perform click action on PIM button"""
    def click_PIM(self):
        self.driver.find_element(By.XPATH, self.button_PIM).click()
        time.sleep(2)

    """This method is useful to perform click action on employee list button"""
    def click_employee_list(self):
        self.driver.find_element(By.XPATH, self.button_employee_list).click()
        time.sleep(2)
