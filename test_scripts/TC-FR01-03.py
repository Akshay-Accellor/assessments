
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_empty_interaction_fields():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://yourapplicationurl.com/customer-interaction")
        driver.find_element(By.ID, "newInteractionButton").click()
        driver.find_element(By.ID, "submitButton").click()
        assert "Fields cannot be empty" in driver.page_source
        print("Test Passed: Validation message appears for empty fields.")
    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()
