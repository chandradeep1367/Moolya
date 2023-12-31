# from explicity_wait import wait_


class Selenium_operation:

    def __init__(self, driver):
        self.driver = driver

    # @wait_
    def click_process(self, element_type, locator):
        self.driver.find_element(element_type, locator).click()

    # @wait_
    def send_keys_process(self, element_type, locator, value):
        self.driver.find_element(element_type, locator).send_keys(value)

    def get_element_text(self, element_type, locator):
        element = self.driver.find_element(element_type, locator)
        value = element.text
        return value
