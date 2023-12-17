from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
serivce_obj=Service()
driver = webdriver.Chrome(service=serivce_obj)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
name=driver.find_element(By.NAME,"username")
driver.execute_script("arguments[0].value='Admin';",name)
time.sleep(5)
pswd = driver.find_element(By.NAME,"password")
driver.execute_script("arguments[0].value='admin123';",pswd)
time.sleep(5)
button = driver.find_element(By.CSS_SELECTOR,".oxd-button")
driver.execute_script("arguments[0].click();",button)
time.sleep(5)



