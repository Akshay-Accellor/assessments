from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_invalid_needs_assessment():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get('http://yourapp.com/customer-needs')
        driver.find_element(By.ID, 'invalid-option').click()  # Simulate selecting an invalid option
        driver.find_element(By.ID, 'submit-button').click()  # Attempt to submit
        time.sleep(2)
        assert "Invalid selection" in driver.page_source  # Check for error message
    finally:
        driver.quit()
