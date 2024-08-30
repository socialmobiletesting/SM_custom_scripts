from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

def basic_selenium_script():
    # Replace with the path to your webdriver
    # driver = webdriver.Chrome(executable_path="C:\\Program Files\\chromedriver-win64\\chromedriver.exe")
    service = Service("C:\\Program Files\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    # Navigate to Google
    driver.get("https://www.google.com")

    # Find the search bar
    search_bar = driver.find_element(By.NAME, "q")

    # Enter a search term
    search_bar.send_keys("selenium webdriver")

    # Submit the search
    search_bar.send_keys(Keys.RETURN)

    # Wait for results to load (adjust the time as needed)
    time.sleep(5)

    # Close the browser
    # driver.quit()

basic_selenium_script()


