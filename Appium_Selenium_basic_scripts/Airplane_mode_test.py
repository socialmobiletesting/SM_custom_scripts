from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
import subprocess

import time

# from my_selenium_driver import selenium_test
# from my_appium_driver import appium_test
from my_appium_driver_updated import appium_start
from my_appium_driver_updated import appium_stop
from my_selenium_driver_updated import selenium_start
from my_selenium_driver_updated import selenium_stop


def Mambo_airplane_mode():
    # # Appium driver initialization
    # appium_driver = appium_start()

    # driver initialization
    selenium_driver = selenium_start()

    try:
        selenium_driver.get("https://innominds.mambomobility.com/auth/login")
        selenium_driver.maximize_window()
        time.sleep(5)

        selenium_driver.find_element(by=By.XPATH, value="//input[@type='email']").send_keys("asaha@innominds.com")
        selenium_driver.find_element(by=By.XPATH, value="//input[@type='password']").send_keys("Innominds@123")
        time.sleep(2)

        selenium_driver.find_element(by=By.XPATH, value="//span[contains(text(),'Continue')]").click()
        time.sleep(10)

        selenium_driver.find_element(by=By.XPATH,
                                     value="(//span[@class='v-btn__content'][normalize-space()='Management'])[1]").click()
        time.sleep(5)
        selenium_driver.find_element(by=By.XPATH,
                                     value="(//span[@class='v-btn__content'][normalize-space()='Policy Components'])[1]").click()
        time.sleep(5)
        selenium_driver.find_element(by=By.XPATH, value="//input[@placeholder='Search']").send_keys(
            "020124_Avisek_Security")
        time.sleep(5)
        selenium_driver.find_element(by=By.XPATH, value="(//span[contains(text(),'More')])[1]").click()
        time.sleep(5)
        selenium_driver.find_element(by=By.XPATH, value="//span[contains(text(),'Configure')]").click()
        time.sleep(5)

        selenium_driver.find_element(by=By.XPATH, value="(//div[@role='combobox'])[2]").click()
        time.sleep(3)
        print("Configure")
        selenium_driver.find_element(by=By.XPATH, value="//span[normalize-space()='Airplane mode is disabled']").click()
        time.sleep(5)
        print('Configured')

        try:
            selenium_driver.find_element(by=By.XPATH, value="//span[contains(text(),'Update')]").click()
            time.sleep(10)
        except Exception as e:
            print("No changes in component", e)

    except Exception as e:
        print(e)

    # Appium driver initialization
    appium_driver = appium_start()

    try:
        time.sleep(3)
        subprocess.check_output("adb shell am start -n com.android.settings/com.android.settings.Settings")
        time.sleep(3)
        network_and_internet = appium_driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                                          value='new UiSelector().text("Network & internet")')
        network_and_internet.click()
        time.sleep(2)

        airplane_mode = appium_driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                                   value='new UiSelector().text("Airplane mode")')
        airplane_mode_switch = appium_driver.find_element(by=AppiumBy.ID, value='android:id/switch_widget')

        airplane_mode_state = airplane_mode_switch.get_attribute("checked")

        if airplane_mode_state == "false":
            print("Airplane mode off")
        else:
            print("Airplane mode on!!!!!!")

    except Exception as e:
        print(e)

    # Close appium driver
    # appium_driver.quit()
    appium_stop()
    # Close the browser
    # selenium_driver.quit()
    selenium_stop()


Mambo_airplane_mode()
