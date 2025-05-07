from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_submit_customer_needs():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://yourappurl.com")
        time.sleep(2)
        driver.find_element(By.ID, "loginButton").click()
        driver.find_element(By.ID, "submitNeedsButton").click()
        time.sleep(1)
        driver.find_element(By.ID, "needsTextBox").send_keys("Need assistance with product functionality.")
        driver.find_element(By.ID, "submitButton").click()
        time.sleep(2)
        assert "Submission confirmed" in driver.page_source  # Check for confirmation message
        print("Customer needs submitted successfully.")
    finally:
        driver.quit()