import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from utility.BasePage import BasePage
from selenium.webdriver.common.keys import Keys


class SearchProduct(BasePage):
    click_search_box_locator = (By.XPATH, "//div[@class='SearchBar__AnimationWrapper-sc-16lps2d-1 iJnYYS']")
    search_box_locator = (By.XPATH, "//*[@id='app']/div/div/div[1]/header/div[2]/div/input")
    add_items=(By.XPATH,"(//*[@id='app']/div/div/div[3]/div/div/div[2]/div[1]/div/div/div/div[2]/div[2]/a[1]/div/div[2]/div[2]/div[2]/div[2])[2]")
    increment_item=(By.XPATH,"/html/body/div[1]/div/div/div[3]/div/div/div[2]/div[1]/div/div/div/div[2]/div[2]/a[1]/div/div[2]/div[2]/div[2]/div[2]/div[2])")
    cart_item=(By.XPATH,"//*[@id='app']/div/div/div[1]/header/div[3]/div/div")
    proceed_to_buy=(By.XPATH,"/html/body/div[3]/div/div/div/div/div/div[2]/div[11]/div/div/div/div/div/div/div[1]")
    add_new_address=(By.XPATH,"/html/body/div[3]/div/div/div/div/div/div[2]/div[1]/div[1]/div")

    def __init__(self, driver):
        super().__init__(driver)
        # driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def get_title(self, title):
        return self.get_title(title)

    def search_product(self, search_text):
        self.do_click(self.click_search_box_locator)
        self.do_send_keys(self.search_box_locator, search_text)
        # self.do_click(self.search_box_locator)
        # self.do_enter(self.search_box_locator)
        time.sleep(10)

    def add_item(self):
        self.do_click(self.add_items)
        self.do_click(self.increment_item)

    def cart_item1(self):
        self.do_click(self.cart_item)

    def purchase_item(self):
        self.do_click(self.proceed_to_buy)





