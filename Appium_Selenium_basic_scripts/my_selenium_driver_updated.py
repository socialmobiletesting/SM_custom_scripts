from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

# Global variable to hold the Selenium session
selenium_driver = None


def selenium_start():
    global selenium_driver

    if selenium_driver is None:
        print("Starting Selenium session...")
        service = Service("C:\\Program Files\\chromedriver-win64\\chromedriver.exe")
        selenium_driver = webdriver.Chrome(service=service)
        print("Selenium session started:", selenium_driver)
    else:
        print("Selenium session started: ", selenium_driver)
    return selenium_driver


def selenium_test():
    # Driver initialization
    # service = Service("C:\\Program Files\\chromedriver-win64\\chromedriver.exe")
    # selenium_driver = webdriver.Chrome(service=service)
    # print(selenium_driver)
    # return selenium_driver
    selenium_driver = selenium_start()

    # Navigate to Google
    selenium_driver.get("https://www.google.com")

    # Find the search bar
    search_bar = selenium_driver.find_element(By.NAME, "q")

    # Enter a search term
    search_bar.send_keys("selenium webdriver")

    # Submit the search
    search_bar.send_keys(Keys.RETURN)

    # Wait for results to load (adjust the time as needed)
    time.sleep(5)

    # Close the browser
    # selenium_driver.quit()


def selenium_stop():
    global selenium_driver
    if selenium_driver is not None:
        print("Stopping Selenium session...", selenium_driver)
        selenium_driver.quit()
        selenium_driver = None
        print("Selenium session stopped.")
    else:
        print("No Selenium session to stop.")


# def selenium_test():
# Driver initialization
# service = Service("C:\\Program Files\\chromedriver-win64\\chromedriver.exe")
# selenium_driver = webdriver.Chrome(service=service)
# print(selenium_driver)
# return selenium_driver

# # Navigate to Google
# selenium_driver.get("https://www.google.com")

# # Find the search bar
# search_bar = selenium_driver.find_element(By.NAME, "q")
#
# # Enter a search term
# search_bar.send_keys("selenium webdriver")
#
# # Submit the search
# search_bar.send_keys(Keys.RETURN)
#
# # Wait for results to load (adjust the time as needed)
# time.sleep(5)

# # Close the browser
# selenium_driver.quit()

# def webdriver_start(serial=""):
#     """
#     This function is used to start the chrome webdriver
#     :return:
#     """
#     import configparser
#     config = configparser.ConfigParser()
#     print("loading config proos")
#     path = get_root_directory_path()
#     directory_path = os.path.join(path, 'config.properties')
#     config.read(directory_path)
#     print("Sections:", config.sections())
#     chrome_path = config.get('lib_config', 'web_driver_start')
#
#     if "Chrome" in serial:
#         print("Chrome")
#         # driver = webdriver.Chrome(executable_path='start chrome')
#         # driver = webdriver.Chrome(executable_path="C:\Program Files\Google\Chrome\Application\chromedriver.exe")
#         s = Service(f'{chrome_path}')
#         opt = webdriver.ChromeOptions()
#         driver = webdriver.Chrome(service=s, options=opt)
#         driver.maximize_window()
#     elif "FireFox" in serial:
#         print("FireFox")
#         driver = webdriver.Firefox(executable_path='start firefox')
#     elif "Edge" in serial:
#         print("Edge")
#         driver = webdriver.Edge(executable_path='start microsoft-edge:')
#     print(driver)
#     return driver

if __name__ == "__main__":
    selenium_start()
    selenium_test()
    selenium_stop()


