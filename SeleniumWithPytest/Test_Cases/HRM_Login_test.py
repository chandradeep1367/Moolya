import pytest

from Page_Objects.HRM_Login_Page import HRM_Login
from utilities.properties.readProperties import ReadConfig


@pytest.mark.usefixtures("init_Driver")
class LoginPage:
    pass


class Test_Login_001(LoginPage):

    username = ReadConfig.get_user_name()
    password = ReadConfig.get_password()
    url = ReadConfig.get_app_URL()

    def test_home_page_title(self):
        self.driver.get(url=self.url)
        self.driver.implicitly_wait(10)
        act_home_page_title = self.driver.title
        print("Orange HRM Actual Home Page Title is :: ", act_home_page_title)

        exp_home_page_title = "OrangeHRM"
        print("Orange HRM Expected Home Page Title is :: ", exp_home_page_title)

        if act_home_page_title == exp_home_page_title:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_home_page_title_success.png")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_home_page_title_failure.png")
            assert False

    def test_HRM_login(self):
        self.driver.get(url=self.url)
        self.driver.implicitly_wait(10)
        self.lp = HRM_Login(driver=self.driver)
        self.lp.set_user_name_and_pwd(self.username, self.password)
        self.lp.click_login()
        act_login_title = self.driver.title
        print("Orange HRM Actual Login Page Title is :: ", act_login_title)

        exp_login_page_title = "OrangeHRM"
        print("Orange HRM Expected Login Page Title is :: ", exp_login_page_title)

        if act_login_title == exp_login_page_title:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_page_title_success.png")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_page_title_failure.png")
            assert False
