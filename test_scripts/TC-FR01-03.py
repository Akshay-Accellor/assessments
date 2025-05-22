
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_logged_in_homepage():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com")
        # Assume login is implemented here
        driver.find_element(By.ID, "username").send_keys("testuser")
        driver.find_element(By.ID, "password").send_keys("password123")
        driver.find_element(By.ID, "login_button").click()
        assert "Welcome" in driver.page_source
        print("Test passed: Personalized options displayed")
    except AssertionError:
        print("Test failed")
    finally:
        driver.quit()
