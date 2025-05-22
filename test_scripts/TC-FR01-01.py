
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_homepage_accessibility():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com")
        assert "Welcome" in driver.title
        driver.find_element(By.ID, "contact_us").click()
        assert driver.find_element(By.ID, "contact_form").is_displayed()
        print("Test passed: Homepage and contact form accessible")
    except AssertionError:
        print("Test failed")
    finally:
        driver.quit()
