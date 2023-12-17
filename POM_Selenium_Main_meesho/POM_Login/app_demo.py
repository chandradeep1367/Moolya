import time
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    appium_server_url = "http://localhost:4723/wd/hub"
    capabilities = dict(
        deviceName='Krushna',
        platformName='Android',
        appPackage='com.androidsample.generalstore',
        appActivity='com.androidsample.generalstore.SplashActivity',
    )
    driver = webdriver.Remote(appium_server_url, options=AppiumOptions().load_capabilities(capabilities))
    time.sleep(7)
    # driver.find_element(AppiumBy.ID, "android:id/text1").click()
    driver.find_element(AppiumBy.ID, "com.androidsample.generalstore:id/spinnerCountry").click()
    time.sleep(3)









