from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_ob=Service()
driver = webdriver.Chrome(service=service_ob)
driver.implicitly_wait(10)
driver.maximize_window()
# driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
# time.sleep(10)
# driver.find_element(By.XPATH,"//*[@class='search-keyword']").send_keys("ca")
# time.sleep(10)
# items=driver.find_elements(By.XPATH,"//*[@class='products']/div")
# time.sleep(5)
# print(len(items))
# # print(items)
# time.sleep(5)

# for i in items:
#     # time.sleep(2)
#     i.find_element(By.XPATH,'div/button').click()
# time.sleep(5)
#
# add_to_cart=driver.find_element(By.XPATH,"//img[@alt='Cart']").click()

# driver.find_element(By.XPATH,"//*[@type='button']").click()
#
# time.sleep(5)

# val_item=driver.find_elements(By.XPATH,"//table/tbody/tr/td[5]")
# print(len(val_item))
# sum=0
# total =826

# for i in val_item:
#     b=i.text
#     print(b)
#     c=int(b)
#     sum +=c
# print(sum)
# assert sum == total
# if sum == total:
#     print("Verify Passed: element value is same value")
# else:
#     print("Verify Failed: element value is not same value")
#
# Place_Order=driver.find_element(By.XPATH,"/html/body/div/div/div/div/div/button").click()
#
# chose_country=driver.find_element(By.XPATH,"/html/body/div/div/div/div/div/div/select")
# select = Select(chose_country)
# select.select_by_visible_text("India")
# driver.find_element(By.XPATH, "//input[@class='chkAgree']").click()
# driver.find_element(By.XPATH, "//button[text()='Proceed']").click()
# time.sleep(5)






##########################################################
# driver.get("https://www.espncricinfo.com/")
# time.sleep(10)
# action = ActionChains(driver)
# for i in range(6):
#     action.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(3)
# driver.find_element(By.XPATH,"//*[@class='ds-text-tight-m ds-font-regular']").click()
# time.sleep(4)
# driver.close()





###########################################################
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# time.sleep(10)
# driver.find_element(By.NAME, "username").send_keys('Admin')
# driver.find_element(By.NAME, "password").send_keys('admin123')
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
# time.sleep(3)
# driver.find_element(By.XPATH, "//a[@class='oxd-main-menu-item active']").click()
# time.sleep(3)
# name = driver.find_element(By.XPATH, "(//input[@placeholder='Type for hints...'])[1]")
# name.click()
# time.sleep(2)
# name.send_keys('S')
# time.sleep(10)
# driver.find_element(By.XPATH, "oxd-autocomplete-text-input oxd-autocomplete-text-input--active").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "(//div[@class='oxd-select-text-input'])[3]").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "//div[text()='Automation Tester']").click()
# driver.close()




