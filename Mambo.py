from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time




def mambo_airplane_mode():
    # Driver initialization
    service = Service("C:\\Program Files\\chromedriver-win64\\chromedriver.exe")

    selenium_driver = webdriver.Chrome(service=service)

    # Opening mambo
    selenium_driver.get("https://innominds.mambomobility.com/auth/login")
    selenium_driver.maximize_window()
    time.sleep(5)

    selenium_driver.find_element(by=By.XPATH, value="//input[@type='email']").send_keys("asaha@innominds.com")
    selenium_driver.find_element(by=By.XPATH, value="//input[@type='password']").send_keys("Innominds@123")
    time.sleep(2)

    selenium_driver.find_element(by=By.XPATH, value="//span[contains(text(),'Continue')]").click()
    time.sleep(15)

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
    print("COnfigure")
    selenium_driver.find_element(by=By.XPATH, value="//span[normalize-space()='Airplane mode is disabled']").click()
    time.sleep(10)
    print('QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ')


    selenium_driver.find_element(by=By.XPATH, value="//span[contains(text(),'Update')]").click()
    time.sleep(10)

    # Wait for results to load (adjust the time as needed)
    time.sleep(5)

    # Close the browser
    selenium_driver.quit()


if __name__ == "__main__":
    mambo_airplane_mode()
