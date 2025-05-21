
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_empty_needs_assessment():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://example.com/customer-needs-assessment")
        driver.find_element(By.ID, "submit-needs").click()
        time.sleep(2)
        assert "Cannot submit empty assessment" in driver.page_source
        print("Error message for empty submission displayed correctly.")
    finally:
        driver.quit()
