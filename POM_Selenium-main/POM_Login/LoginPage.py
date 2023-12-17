from selenium import webdriver
from selenium.webdriver.common.by import By

from utility.BasePage import BasePage


class Login(BasePage):
    username = (By.NAME, "username")
    password = (By.NAME, "password")
    login_submit_btn = (By.XPATH, "//*[@type='submit']")
    Logout_dropdwn_btn = (By.XPATH, "//*[@class='oxd-userdropdown-name']")
    Logout_link = (By.LINK_TEXT, "Logout")

    def __init__(self, driver):
        super().__init__(driver)
        # driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def get_title(self, title):
        return self.get_title(title)

    def login(self, username, password):
        self.do_send_keys(self.username, username)
        self.do_send_keys(self.password, password)
        self.do_click(self.login_submit_btn)

    # def Enter_username(self,name):
    #     self.driver.find_element(By.NAME, *Login.username).send_keys(name)
    #
    # def Enter_password(self, pwd):
    #     self.driver.find_element(By.NAME, *Login.password).send_keys(pwd)
    #
    # def Click_submitbtn(self):
    #     self.driver.find_element(By.NAME, *Login.login_submit_btn).click()
    #
    # def Click_drpdwn(self):
    #     self.driver.find_element(By.NAME, *Login.Logout_dropdwn_btn).click()
    #
    # def Click_Logout(self):
    #     self.driver.find_element(By.NAME, *Login.Logout_link).click()