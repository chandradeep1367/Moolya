from selenium.webdriver.common.by import By

from utilities.properties.readProperties import ReadConfig


class HRM_Login:

    text_username = ReadConfig.get_textbox_username_xpath()
    text_pwd = ReadConfig.get_textbox_pwd_xpath()
    button_login = ReadConfig.get_button_login_xpath()

    def __init__(self, driver):
        self.driver = driver

    def set_user_name_and_pwd(self, username, password):
        self.driver.find_element(By.XPATH, self.text_username).clear()
        self.driver.find_element(By.XPATH, self.text_username).send_keys(username)

        self.driver.find_element(By.XPATH, self.text_pwd).clear()
        self.driver.find_element(By.XPATH, self.text_pwd).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.button_login).click()
