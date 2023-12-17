# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from time import sleep
#
# service_obj = Service()
# driver = webdriver.Chrome(service=service_obj)
# driver.get('https://blinkit.com/')
# driver.maximize_window()
#
#
#
# sleep(2)
# driver.find_element('xpath', "//button[text()='Detect my location']").click()
# sleep(3)
# driver.find_element('xpath', "//div[@class='SearchBar__AnimationWrapper-sc-16lps2d-1 iJnYYS']").click()
# sleep(3)
# driver.find_element('xpath', "//input[@class='SearchBarContainer__Input-sc-hl8pft-3 irVxjq']").send_keys('toothpast')
# sleep(6)
# driver.find_element('xpath', "(//div[text()='ADD'])[1]").click()
# sleep(2)
# driver.find_element('xpath', "//div[@class='CartButton__CartIcon-sc-1fuy2nj-6 iyUoPU']").click()
# sleep(3)
#
# driver.close()


# -------------------------------------------------------------------------------------------------------

from utility.Base_class import Selenium_operation

location = ('xpath', "//button[text()='Detect my location']")
search_bar = ('xpath', "//div[@class='SearchBar__AnimationWrapper-sc-16lps2d-1 iJnYYS']")
input_search_bar = ('xpath', "//input[@class='SearchBarContainer__Input-sc-hl8pft-3 irVxjq']")
add_button = ('xpath', "(//div[text()='ADD'])[1]")
my_card = ('xpath', "//div[@class='CartButton__CartIcon-sc-1fuy2nj-6 iyUoPU']")


'''class for all the web element inside a web page'''


class Order_on_blinkit(Selenium_operation):

    def find_location(self):
        self.click_process(location)

    def click_search_bar(self):
        self.click_process(search_bar)

    def product_search(self, mouth_fresh):
        self.send_keys_process(input_search_bar, value=mouth_fresh)

    def add(self):
        self.click_process(add_button)

    def card(self):
        self.click_process(my_card)


