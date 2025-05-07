from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_access_customer_platform():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://yourappurl.com")
        time.sleep(2)
        driver.find_element(By.ID, "customersTab").click()
        time.sleep(1)
        assert driver.find_element(By.ID, "sendMessageButton").is_displayed()  # Ensure the send message button is visible
        print("Accessed customer platform successfully.")
    finally:
        driver.quit()