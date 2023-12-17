import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

from utilities.properties.readProperties import ReadConfig


class Search_Product:
    """ Reading Web Element Locators From Config File"""

    """ admin button xpath """
    button_admin = ReadConfig.get_button_admin_xpath()

    """ user_management dropdown xpath """
    drp_user_management = ReadConfig.get_drp_user_management_xpath()

    """ user button xpath """
    button_user = ReadConfig.get_button_user_xpath()

    """ sending username text xpath """
    text_set_username = ReadConfig.get_text_set_username_xpath()

    """ user_role dropdown xpath """
    drp_user_role = ReadConfig.get_drp_user_role_xpath()

    """ selecting use-role as Admin xpath """
    select_user_role_admin = ReadConfig.get_select_user_role_admin()

    """ checking Records for use-role column as Admin xpath """
    check_admin_column = ReadConfig.get_check_admin_column_xpath()

    """ selecting use-role as Admin xpath """

    select_user_role_ess = "//div[@role = 'listbox']//div[3]"

    """ checking Records for use-role column as ESS xpath """
    check_ess_column_xpath = "//div[@class = 'orangehrm-container']//div//div[2][@role = 'rowgroup']//div[@role= " \
                             "'row']//div[3]"

    """ employee_name text xpath """
    search_employee_name_xpath = "//div[@class='oxd-table-filter-area']//div[3]//div[2]//input"

    """ search employee name text xpath"""
    select_employee_name_xpath = "//div[@role = 'option']//span"

    """ checking Records for employee_name column xpath """
    check_employee_name_column_xpath = "//div[@class = 'oxd-table-card']//div[4]"

    """ status dropdown xpath """
    drp_status_xpath = "//div[@class='oxd-table-filter-area']//div[4]//div[2]//div[@class = 'oxd-select-text-input']"

    """ selecting use-role as Admin xpath """
    select_status_enabled = "//div[@role = 'listbox']//div[2]"

    """ checking Records for use-role column as Admin xpath """
    check_enabled_column_xpath = "//div[@class = 'orangehrm-container']//div//div[2][@role = 'rowgroup']//div[@role= " \
                                 "'row']//div[5]"

    """ selecting use-role as Admin xpath """
    select_status_disabled = "//div[@role = 'listbox']//div[3]"

    """ checking Records for use-role column as ESS xpath """
    check_disabled_column_xpath = "//div[@class = 'orangehrm-container']//div//div[2][@role = 'rowgroup']//div[@role= " \
                                  "'row']//div[5]"

    button_search_xpath = "//button[@type='submit']"
    check_search_admin_xpath = "//div[@class = 'oxd-table-body']//div[@class = 'oxd-table-cell oxd-padding-cell'][2]"

    def __init__(self, driver):
        self.driver = driver

    def click_admin(self):
        self.driver.find_element(By.XPATH, self.button_admin).click()
        time.sleep(2)

    def click_user_management(self):
        user_management = self.driver.find_element(By.XPATH, self.drp_user_management)
        actions = ActionChains(self.driver)
        actions.move_to_element(user_management).click().perform()

    def click_user(self):
        user = self.driver.find_element(By.XPATH, self.button_user)
        actions = ActionChains(self.driver)
        actions.move_to_element(user).click().perform()
        time.sleep(2)

    def search_username(self, search_username):
        self.driver.find_element(By.XPATH, self.text_set_username).send_keys(search_username)
        time.sleep(2)

    def get_search_username_record(self):
        act_record = self.driver.find_element(By.XPATH, self.check_search_admin_xpath).text
        if act_record == "Admin":
            assert True
            print("act search username value is :: ", act_record)
        else:
            assert False
        time.sleep(10)

    def search_user_role_admin(self):
        self.driver.find_element(By.XPATH, self.drp_user_role).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.select_user_role_admin).click()

    def check_user_role_admin_column_table(self):
        admin_list = self.driver.find_elements(By.XPATH, self.check_admin_column_xpath)
        print("User Role - Admin column count is :: ", len(admin_list))
        for i in range(0, len(admin_list)):
            print("User Role Column -> {} Values is -> {}".format(i, admin_list[i].text))
            if admin_list[i].text == "Admin":
                assert True
            else:
                assert False
        time.sleep(10)

    def search_user_role_ess(self):
        self.driver.find_element(By.XPATH, self.drp_user_role).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.select_user_role_ess).click()

    def check_user_role_ess_column_table(self):
        ess_list = self.driver.find_elements(By.XPATH, self.check_ess_column_xpath)
        print("User Role - ESS column count is :: ", len(ess_list))
        for i in range(0, len(ess_list)):
            print("User Role Column -> {} Values is -> {}".format(i, ess_list[i].text))
            if ess_list[i].text == "ESS":
                assert True
            else:
                assert False
        time.sleep(10)

    def search_employee_name(self, search_employee_name):
        self.driver.find_element(By.XPATH, self.search_employee_name_xpath).send_keys(search_employee_name)
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.select_employee_name_xpath).click()

    def get_search_employee_name_record(self):
        act_record = self.driver.find_element(By.XPATH, self.check_employee_name_column_xpath).text
        if act_record == "Virat Kohli":
            assert True
            print("act search username value is :: ", act_record)
        else:
            assert False
        time.sleep(10)

    def click_search(self):
        self.driver.find_element(By.XPATH, self.button_search_xpath).click()
        time.sleep(3)

    def search_status_enabled(self):
        self.driver.find_element(By.XPATH, self.drp_status_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.select_status_enabled).click()

    def check_status_enabled_column_table(self):
        enabled_list = self.driver.find_elements(By.XPATH, self.check_status_enabled_column_table())
        print("User Role - Admin column count is :: ", len(enabled_list))
        for i in range(0, 11):
            print("User Role Column -> {} Values is -> {}".format(i, enabled_list[i].text))
            if enabled_list[i].text == "Enabled":
                assert True
            else:
                assert False
        time.sleep(10)

    def search_status_disabled(self):
        self.driver.find_element(By.XPATH, self.drp_status_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.select_status_disabled).click()

    def check_status_disabled_column_table(self):
        disabled_list = self.driver.find_elements(By.XPATH, self.check_disabled_column_xpath)
        print("User Role - ESS column count is :: ", len(disabled_list))
        for i in range(0, len(disabled_list)):
            print("User Role Column -> {} Values is -> {}".format(i, disabled_list[i].text))
            if disabled_list[i].text == "Disabled":
                assert True
            else:
                assert False
        time.sleep(10)
