import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # def getLogger(self):
    #     loggerName = inspect.stack()[1][3]
    #     logger = logging.getLogger(loggerName)
    #     fileHandler = logging.FileHandler('logfile.log')
    #     formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    #     fileHandler.setFormatter(formatter)
    #
    #     logger.addHandler(fileHandler)  # filehandler object
    #
    #     logger.setLevel(logging.DEBUG)
    #     return logger

    # def verifyLinkPresence(self, text):
    #     element = WebDriverWait(self.driver, 10).until(
    #     EC.presence_of_element_located((By.LINK_TEXT, text)))

    # def selectOptionByText(self,locator,text):
    #     sel = Select(locator)
    #     sel.select_by_visible_text(text)

    def do_click(self,locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def do_send_keys(self, locator, text):
        WebDriverWait(self.driver,  10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_title(self, title):
        WebDriverWait(self.driver,  10).until(EC.title_is(title))
        return self.driver.title