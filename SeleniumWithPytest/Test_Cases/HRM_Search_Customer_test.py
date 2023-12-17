import time

import pytest

from Page_Objects.HRM_Login_Page import HRM_Login
from Page_Objects.Blinkit_Search_Product import Search_Customer
from utilities.properties.readProperties import ReadConfig


@pytest.mark.usefixtures("init_Driver")
class OrangeHRM_Search_Customer:
    pass


class Test_Search_Customer_001(OrangeHRM_Search_Customer):

    username = ReadConfig.get_user_name()
    password = ReadConfig.get_password()
    url = ReadConfig.get_app_URL()
    search_username = ReadConfig.get_search_username()
    search_employee_name = ReadConfig.get_search_employee_name()

    def test_search_customer_by_username(self):
        self.driver.get(url=self.url)
        self.driver.implicitly_wait(10)
        self.sc = Search_Customer(driver=self.driver)
        self.sc.click_admin()
        self.sc.click_user_management()
        self.sc.click_user()
        self.sc.search_username(search_username=self.search_username)
        self.sc.click_search()
        self.sc.get_search_username_record()
        time.sleep(5)

    def test_search_customer_by_user_role_admin(self):
        self.driver.get(url=self.url)
        self.driver.implicitly_wait(10)
        self.lp = HRM_Login(driver=self.driver)
        self.lp.set_user_name_and_pwd(self.username, self.password)
        self.lp.click_login()
        self.sc = Search_Customer(driver=self.driver)
        self.sc.click_admin()
        self.sc.click_user_management()
        self.sc.click_user()
        self.sc.search_user_role_admin()
        self.sc.click_search()
        self.sc.check_user_role_admin_column_table()

    def test_search_customer_by_user_role_ess(self):
        self.driver.get(url=self.url)
        self.driver.implicitly_wait(10)
        self.lp = HRM_Login(driver=self.driver)
        self.lp.set_user_name_and_pwd(self.username, self.password)
        self.lp.click_login()
        self.sc = Search_Customer(driver=self.driver)
        self.sc.click_admin()
        self.sc.click_user_management()
        self.sc.click_user()
        self.sc.search_user_role_ess()
        self.sc.click_search()
        self.sc.check_user_role_ess_column_table()

    def test_search_customer_by_employee_name(self):
        self.driver.get(url=self.url)
        self.driver.implicitly_wait(10)
        self.lp = HRM_Login(driver=self.driver)
        self.lp.set_user_name_and_pwd(self.username, self.password)
        self.lp.click_login()
        self.sc = Search_Customer(driver=self.driver)
        self.sc.click_admin()
        self.sc.click_user_management()
        self.sc.click_user()
        self.sc.search_employee_name(self.search_employee_name)
        self.sc.click_search()
        self.sc.get_search_employee_name_record()

    def test_search_customer_by_status_enabled(self):
        self.driver.get(url=self.url)
        self.driver.implicitly_wait(10)
        self.lp = HRM_Login(driver=self.driver)
        self.lp.set_user_name_and_pwd(self.username, self.password)
        self.lp.click_login()
        self.sc = Search_Customer(driver=self.driver)
        self.sc.click_admin()
        self.sc.click_user_management()
        self.sc.click_user()
        self.sc.search_status_enabled()
        self.sc.click_search()
        # self.sc.check_status_enabled_column_table()

    def test_search_customer_by_status_disabled(self):
        self.driver.get(url=self.url)
        self.driver.implicitly_wait(10)
        self.lp = HRM_Login(driver=self.driver)
        self.lp.set_user_name_and_pwd(self.username, self.password)
        self.lp.click_login()
        self.sc = Search_Customer(driver=self.driver)
        self.sc.click_admin()
        self.sc.click_user_management()
        self.sc.click_user()
        self.sc.search_status_disabled()
        self.sc.click_search()
        self.sc.check_status_disabled_column_table()

