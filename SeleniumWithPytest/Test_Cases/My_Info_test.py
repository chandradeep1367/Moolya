import time

import pytest

from Page_Objects.HRM_Login_Page import HRM_Login
from Page_Objects.Blinkit_Search_Product import Search_Customer
from Page_Objects.My_Info_Page import My_Info
from Test_Cases.HRM_Login_test import Test_Login_001
from utilities.properties.readProperties import ReadConfig


@pytest.mark.usefixtures("init_Driver")
class Employee_Info:
    pass


class Test_Employee_Info(Employee_Info):
    username = ReadConfig.get_user_name()
    password = ReadConfig.get_password()
    url = ReadConfig.get_app_URL()

    def test_personal_details(self):
        self.driver.get(url=self.url)
        self.driver.implicitly_wait(10)
        self.lp = HRM_Login(driver=self.driver)
        self.lp.set_user_name_and_pwd(self.username, self.password)
        self.lp.click_login()
        self.info = My_Info(driver=self.driver)
        self.info.click_my_info()
        # self.driver.switch_to.frame()
        self.info.click_personal_details()
        self.info.get_employee_first_name()
        time.sleep(2)

