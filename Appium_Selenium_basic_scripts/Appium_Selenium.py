
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager

import time

from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy






# Selenium Web Automation
def selenium_example():
    # Setup Chrome WebDriver
    service = Service("C:\\Program Files\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.google.com")

    # Perform a Google search
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium with Python")
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)  # Wait for the results

    # Print the title of the page
    print(driver.title)

    driver.quit()




def appium_example():
    cap: Dict[str, Any] = {
        'platformName': 'Android',
        'automationName': 'uiautomator2',
        'appPackage': 'com.android.settings',
        'appActivity': 'com.android.settings.Settings'
    }

    url = 'http://127.0.0.1:4723'

    appium_driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

    network_and_internet = appium_driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("Network & internet")')
    network_and_internet.click()
    time.sleep(2)

    airplane_mode = appium_driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("Airplane mode")')
    airplane_mode_switch = appium_driver.find_element(by=AppiumBy.ID, value='android:id/switch_widget')


    airplane_mode_state = airplane_mode_switch.get_attribute("checked")

    if airplane_mode_state == "false":
        print("Airplane mode off by default")
    else:
        print("Airplane mode on!!!!!!")

    appium_driver.quit()


if __name__ == "__main__":
    # Run Selenium use case
    selenium_example()

    # Run Appium use case
    appium_example()

