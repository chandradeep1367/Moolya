import pytest
from pom.Blinkit import Order_on_blinkit


def run_script(_driver):
    b = Order_on_blinkit(_driver)
    b.find_location()
    b.click_search_bar()
    b.product_search("toothpast")
    b.add()
    b.card()



# -----------------------------------------------------------------------------------------------------
                                                # for multipul data
# input = [("toothpast")]                         # [("Bengaluru", "Bhubaneswar", 5-12-2023, "Jyotiprakash", 26, "kumarbapin6@gmail.com",7978425565)]
#
#
#
# @pytest.mark.parametrize("mouth_fresh", input)    # ("onboarding_name, dropping_name, date, t_name, t_age, mail_id, num", input)
# def run_script(mouth_fresh, _driver):             # (onboarding_name, dropping_name, date, t_name, t_age, mail_id, num, _driver)
#     b = Order_on_blinkit(_driver)
#     b.find_location()
#     b.click_search_bar()
#     b.product_search(mouth_fresh)
#     b.add()
#     b.card()