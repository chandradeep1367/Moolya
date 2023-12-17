import pytest

from POM_Login.LoginPage import Login
from testcases.conftest import setup
from utility.BasePage import BaseClass


class Login(BaseClass):
    name = "Admin"
    pwd = "admin123"

    def test_Login(self, setup):
        self.driver = setup


def Test_Login(setup):
    obj = Login()

    obj.Enter_username("Admin")
    obj.Enter_password("admin123")
    obj.Click_submitbtn()
    obj.Click_drpdwn()
    obj.Click_Logout()
