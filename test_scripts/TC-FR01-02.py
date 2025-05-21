
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_no_access_without_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://yourapplicationurl.com/customer-interaction")
        assert "Login" in driver.title
        print("Test Passed: User redirected to login")
    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()
