
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_access_denied():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/customer-interaction")
        assert "Access Denied" in driver.page_source
        print("Access Denied Test Passed")
    except Exception as e:
        print(f"Error during access test: {e}")
    finally:
        driver.quit()
