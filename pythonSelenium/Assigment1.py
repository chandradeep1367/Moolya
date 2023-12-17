from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
service_ob=Service()
driver = webdriver.Chrome(service=service_ob)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("ca")
product = driver.find_element(By.XPATH,"//div[@class='products']/div")
# print(len(product))
print(product)


# for i in product:
#     driver.find_element(By.XPATH,"//button[@type='button']").click()
# time.sleep(5)
