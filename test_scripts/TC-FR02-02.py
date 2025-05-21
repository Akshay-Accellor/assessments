
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_invalid_customer_needs():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://yourapplicationurl.com/customer-needs")
        driver.find_element(By.ID, "inputCustomerDetails").send_keys("Invalid Input")
        driver.find_element(By.ID, "analyzeButton").click()
        assert "Invalid details" in driver.page_source
        print("Test Passed: Error message appears for invalid input.")
    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()
