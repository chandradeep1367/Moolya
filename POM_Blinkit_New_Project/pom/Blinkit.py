from datetime import datetime
from selenium.webdriver.common.by import By
from utility.Base_class import Selenium_operation

location = (By.XPATH, "//button[text()='Detect my location']")
search_bar = (By.XPATH, "//div[@class='SearchBar__AnimationWrapper-sc-16lps2d-1 iJnYYS']")
input_search_bar = (By.XPATH, "//input[@class='SearchBarContainer__Input-sc-hl8pft-3 irVxjq']")
colgate = (By.XPATH, "//div[text()='Colgate Active Salt Toothpaste (300 g)']")
add_button = (By.XPATH, "//div[text()='ADD']")
my_cart = (By.XPATH, "//div[text()=' items']")
grand_total = (By.XPATH, "//div[@class='BillCard__BillItemContainer-sc-1ctm5d1-17 dCrowE']//child::div[2]//child::div[1]//child::div")
total = (By.XPATH, "//div[@class='CheckoutStrip__StripContainer-sc-1fzbdhy-8 ZeXgt']//child::div[1]//child::div[1]")

'''class for all the web element inside a web page'''


class Order_on_blinkit(Selenium_operation):

    def find_location(self):
        self.click_process(location[0], location[1])

    def click_search_bar(self):
        self.click_process(search_bar[0], search_bar[1])

    def product_search(self, mouth_fresh):
        self.send_keys_process(input_search_bar[0], input_search_bar[1], value=mouth_fresh)

    def click_on_product(self):
        self.click_process(colgate[0], colgate[1])

    def add(self):
        self.click_process(add_button[0], add_button[1])

    def cart(self):
        self.click_process(my_cart[0], my_cart[1])

    def get_total_and_grand_total(self):
        grand_total_value = self.get_element_text(grand_total[0], grand_total[1])
        total_value = self.get_element_text(total[0], total[1])
        return grand_total_value, total_value

    @staticmethod
    def save_screenshot(driver, file_name):
        driver.save_screenshot(f'./reports/{file_name}_{datetime.now().strftime("%d-%m-%Y %H-%M-%S")}.png')

