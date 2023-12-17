# from explicity_wait import wait_


class Selenium_operation:

    def __init__(self, driver):
        self.driver = driver

    # @wait_
    def click_process(self, locator):
        self.driver.findelement(locator).click()

    # @wait_
    def send_keys_process(self, locators, *, value):
        self.driver.find_element(*locators).send_keys(value)
