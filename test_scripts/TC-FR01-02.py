
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_invalid_url_access():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://invalid.com")
        assert "404" in driver.title
        print("Test passed: Error message displayed")
    except AssertionError:
        print("Test failed")
    finally:
        driver.quit()
