from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

import time


def appium_test():
    cap: Dict[str, Any] = {
        'platformName': 'Android',
        'automationName': 'uiautomator2',
        'appPackage': 'com.android.settings',
        'appActivity': 'com.android.settings.Settings'
    }

    url = 'http://127.0.0.1:4723'

    appium_driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
    return appium_driver

    network_and_internet = appium_driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                                      value='new UiSelector().text("Network & internet")')
    network_and_internet.click()
    time.sleep(2)


    airplane_mode = appium_driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                               value='new UiSelector().text("Airplane mode")')
    airplane_mode_switch = appium_driver.find_element(by=AppiumBy.ID, value='android:id/switch_widget')

    airplane_mode_state = airplane_mode_switch.get_attribute("checked")

    if airplane_mode_state == "false":
        print("Airplane mode off by default")
    else:
        print("Airplane mode on!!!!!!")

        # airplane_mode = appium_driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
        #                                            value='new UiSelector().text("Airplane mode")')
        # airplane_mode.click()

    appium_driver.quit()


# appium_test()
if __name__ == "__main__":
    appium_test()
