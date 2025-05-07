from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_submit_empty_customer_needs():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://yourappurl.com")
        time.sleep(2)
        driver.find_element(By.ID, "loginButton").click()
        driver.find_element(By.ID, "submitNeedsButton").click()
        time.sleep(1)
        driver.find_element(By.ID, "submitButton").click()
        time.sleep(2)
        assert "This field is required" in driver.page_source  # Check for error message
        print("Error handling for empty submission verified.")
    finally:
        driver.quit()