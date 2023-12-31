import time
import logging as logger
from pom.Blinkit import Order_on_blinkit


# def test_logger():
#     logger.info("HI")
#     logger.debug("HI")
#     logger.warning("HI")
#     logger.error("HI")
#     logger.critical("HI")


def test_verify_cart_value(_driver):
    b = Order_on_blinkit(_driver)
    try:
        b.find_location()
        time.sleep(3)
        b.click_search_bar()
        b.product_search("toothpaste")
        b.click_on_product()
        b.add()
        b.cart()
        grand_total_value, total_value = b.get_total_and_grand_total()
        logger.info(f"GRAND_TOTAL:{grand_total_value}")
        logger.info(f"TOTAL:{total_value}")
        assert grand_total_value == total_value
    except Exception as error:
        logger.error(f"Error: {error}")
        b.save_screenshot(_driver, file_name="test_verify_cart_value_error")
        raise error



# -----------------------------------------------------------------------------------------------------
# for multipul data
# input = [("toothpast")]                         # [("Bengaluru", "Bhubaneswar", 5-12-2023, "Jyotiprakash", 26, "kumarbapin6@gmail.com",7978425565)]
# @pytest.mark.parametrize("mouth_fresh", input)    # ("onboarding_name, dropping_name, date, t_name, t_age, mail_id, num", input)
# def run_script(mouth_fresh, _driver):             # (onboarding_name, dropping_name, date, t_name, t_age, mail_id, num, _driver)
#     b = Order_on_blinkit(_driver)
#     b.find_location()
#     b.click_search_bar()
#     b.product_search(mouth_fresh)
#     b.add()
#     b.card()
