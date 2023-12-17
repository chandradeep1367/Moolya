from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
service_ob=Service()
driver = webdriver.Edge(service=service_ob)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR,".oxd-button").click()
driver.find_element(By.CSS_SELECTOR,".oxd-userdropdown-tab").click()
driver.find_element(By.CSS_SELECTOR,".oxd-userdropdown-link").click()
time.sleep(5)
