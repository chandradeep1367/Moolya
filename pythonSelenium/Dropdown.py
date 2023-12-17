from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# service_ob=Service()
# driver = webdriver.Edge(service=service_ob)
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# dd = driver.find_element(By.NAME,"dropdown-class-example")
# D= Select(dd)
# D.select_by_index(2)
# D.select_by_visible_text("Option2")
# D.select_by_value("option2")
# time.sleep(5)

#DYNAMIC dropdownm

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# service_ob=Service()
# driver = webdriver.Chrome(service=service_ob)
# driver.implicitly_wait(10)
# driver.maximize_window()
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.find_element(By.ID,"autocomplete").send_keys("Ind")
# country= driver.find_elements(By.CSS_SELECTOR,".ui-menu-item")
# for i in country:
#     if i.text == "India":
#         i.click()
# res = driver.find_element(By.ID,"autocomplete").is_displayed()
# # print(res)
# res1 = driver.find_element(By.ID,"autocomplete").get_attribute("value")
# # print(res1)
# assert res1 == "India"

#checkbox
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# service_ob=Service()
# driver = webdriver.Chrome(service=service_ob)
# driver.implicitly_wait(10)
# driver.maximize_window()
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.find_element(By.ID,"checkBoxOption2").click()
# clickbox = driver.find_element(By.ID,"checkBoxOption2").is_selected()
# print(clickbox)
# time.sleep(5)

#iterirate and select checkbox
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# service_ob=Service()
# driver = webdriver.Chrome(service=service_ob)
# driver.implicitly_wait(10)
# driver.maximize_window()
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# checkbox = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
# print(len(checkbox))
# for i in checkbox:
#     val = i.get_attribute("id")
#     if val == "checkBoxOption1":
#         i.click()
#         assert i.is_selected()
# time.sleep(8)

# Switch window
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# service_ob=Service()
# driver = webdriver.Chrome(service=service_ob)
# driver.implicitly_wait(10)
# driver.maximize_window()
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.find_element(By.ID,"openwindow").click()
# win = driver.window_handles
# # driver.switch_to.window(win[1])
# # time.sleep(5)
#
# for i in win:
#     driver.switch_to.window(i)
#     titles= driver.title
#     print(titles)
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# service_ob=Service()
# driver = webdriver.Chrome(service=service_ob)
# driver.implicitly_wait(10)
# driver.maximize_window()
# driver.get("https://demoqa.com/frames")
# driver.switch_to.frame("frame2")
# # txt = driver.find_element(By.ID,"sampleHeading").text
# # print(txt)
# # driver.switch_to.default_content()
# # print(driver.title)
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
# driver.execute_script("window.scrollBy(0,-document.body.scrollHeight);")
# time.sleep(5)


# ALerts
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# service_ob=Service()
# driver = webdriver.Chrome(service=service_ob)
# driver.implicitly_wait(10)
# driver.maximize_window()
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.find_element(By.ID,"alertbtn").click()
# alt = driver.switch_to.alert
# # alt.send_keys("chetan")
# alt.accept()
# driver.find_element(By.ID,"confirmbtn").click()
# alt1 = driver.switch_to.alert
# print(alt1.text)
# alt1.accept()
# alt1.dismiss()

#mouse actions
#
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# service_ob=Service()
# driver = webdriver.Chrome(service=service_ob)
# driver.implicitly_wait(10)
# driver.maximize_window()
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# actions=ActionChains(driver)
# actions.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
# actions.click(driver.find_element(By.LINK_TEXT,"Top")).perform()
# time.sleep(8)

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# service_ob=Service()
# driver = webdriver.Chrome(service=service_ob)
# driver.implicitly_wait(10)
# driver.maximize_window()
# driver.get("https://demoqa.com/buttons")
# actions=ActionChains(driver)
# actions.double_click(driver.find_element(By.ID,"doubleClickBtn")).perform()
# time.sleep(6)

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# service_ob=Service()
# driver = webdriver.Chrome(service=service_ob)
# driver.implicitly_wait(10)
# driver.maximize_window()
# driver.get("https://demoqa.com/droppable")
# src = driver.find_element(By.ID,"draggable")
# target = driver.find_element(By.ID,"droppable")
# actions=ActionChains(driver)
# actions.drag_and_drop(src,target).perform()
# time.sleep(6)

#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# service_ob=Service()
# driver = webdriver.Chrome(service=service_ob)
# driver.implicitly_wait(10)
# driver.maximize_window()
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# # driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
# # driver.execute_script("window.scrollBy(0,-document.body.scrollHeight);")
# ele = driver.find_element(By.ID,"mousehover")
#
# driver.execute_script("arguments[0].scrollIntoView();",ele)
#
# time.sleep(5)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
service_ob=Service()
driver = webdriver.Chrome(service=service_ob)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# txt = driver.find_element(By.XPATH,"//div[@class='tableFixHead']/table/tbody/tr[2]/td[3]").text
# print(txt)
# txt1 = driver.find_element(By.XPATH,"//div[@class='tableFixHead']/table/tbody/tr[2]/td[3]/preceding-sibling::td[2]").text
# print(txt1)
table = driver.find_element(By.XPATH,"//div[@class='tableFixHead']/table")
print(driver.execute_script("return arguments[0].innerText;",table))




















