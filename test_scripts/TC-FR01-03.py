from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_timeout_customers_platform():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://yourappurl.com")
        time.sleep(2)
        driver.find_element(By.ID, "loginButton").click()
        driver.find_element(By.ID, "customersTab").click()
        time.sleep(30)  # Simulate waiting
        assert "Request timed out" in driver.page_source  # Check for timeout message
        print("Timeout behavior verified.")
    finally:
        driver.quit()