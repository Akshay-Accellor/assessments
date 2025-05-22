
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_access_needs_assessment_without_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/needs_assessment")
        assert "Please login" in driver.page_source
        print("Test passed: Redirect to login page")
    except AssertionError:
        print("Test failed")
    finally:
        driver.quit()
