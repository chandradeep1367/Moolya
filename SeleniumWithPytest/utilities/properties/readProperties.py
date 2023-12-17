import os
import configparser

# this_folder = os.path.dirname(os.path.abspath('C:/Users/User/PycharmProjects/SeleniumWithPytest/Configurations'))
# ini_file = os.path.join(this_folder, 'config.ini')

config = configparser.RawConfigParser()
config.read('..//Configurations//config.ini')


class ReadConfig:

    @staticmethod
    def get_app_URL():
        url = config.get('HRM common info', 'baseURL')
        return url

    # @staticmethod
    # def get_user_name():
    #     user_name = config.get('HRM common info', 'username')
    #     return user_name
    #
    # @staticmethod
    # def get_password():
    #     pwd = config.get('HRM common info', 'password')
    #     return pwd

    @staticmethod
    def get_click_search_box_locator():
        click_search_box_locator = config.get('Blinkit common info', 'click_search_box_locator')
        return click_search_box_locator

    @staticmethod
    def get_search_box_locator():
        search_box_locator = config.get('Blinkit common info', 'search_box_locator')
        return search_employee_name

    @staticmethod
    def get_add_items():
        add_items = config.get('Blinkit Web Locators', 'add_items')
        return get_add_items

    @staticmethod
    def get_increment_item():
        increment_item = config.get('Blinkit Web Locators', 'increment_item')
        return increment_item

    @staticmethod
    def get_cart_item():
        cart_item = config.get('Blinkit Web Locators', 'cart_item')
        return cart_item

    @staticmethod
    def get_proceed_to_buy():
        proceed_to_buy = config.get('Blinkit Web Locators', 'proceed_to_buy')
        return proceed_to_buy

    @staticmethod
    def get_add_new_address():
        add_new_address = config.get('Blinkit Web Locators', 'add_new_address')
        return drp_user_management_xpath

    # @staticmethod
    # def get_button_user_xpath():
    #     button_user_xpath = config.get('HRM Web Locators', 'button_user_xpath')
    #     return button_user_xpath
    #
    # @staticmethod
    # def get_text_set_username_xpath():
    #     text_set_username_xpath = config.get('HRM Web Locators', 'text_set_username_xpath')
    #     return text_set_username_xpath
    #
    # @staticmethod
    # def get_drp_user_role_xpath():
    #     drp_user_role_xpath = config.get('HRM Web Locators', 'drp_user_role_xpath')
    #     return drp_user_role_xpath
    #
    # @staticmethod
    # def get_select_user_role_admin():
    #     select_user_role_admin = config.get('HRM Web Locators', 'select_user_role_admin')
    #     return select_user_role_admin
    #
    # @staticmethod
    # def get_check_admin_column_xpath():
    #     check_admin_column_xpath = config.get('HRM Web Locators', 'check_admin_column_xpath')
    #     return check_admin_column_xpath
    #
    # @staticmethod
    # def get_button_PIM_xpath():
    #     button_PIM_xpath = config.get('HRM Web Locators', 'button_PIM_xpath')
    #     return button_PIM_xpath
    #
    # @staticmethod
    # def get_button_employee_list_xpath():
    #     button_employee_list_xpath = config.get('HRM Web Locators', 'button_employee_list_xpath')
    #     return button_employee_list_xpath
    #
    # @staticmethod
    # def get_button_my_info_xpath():
    #     button_my_info_xpath = config.get('HRM Web Locators', 'button_my_info_xpath')
    #     return button_my_info_xpath
    #
    # @staticmethod
    # def get_button_personal_details_xpath():
    #     button_personal_details_xpath = config.get('HRM Web Locators', 'button_personal_details_xpath')
    #     return button_personal_details_xpath
    #
    # @staticmethod
    # def get_text_employee_first_name_xpath():
    #     text_employee_first_name_xpath = config.get('HRM Web Locators', 'text_employee_first_name_xpath')
    #     return text_employee_first_name_xpath
    #
    # @staticmethod
    # def get_button_leave_xpath():
    #     button_leave_xpath = config.get('HRM Web Locators', 'button_leave_xpath')
    #     return button_leave_xpath
    #
