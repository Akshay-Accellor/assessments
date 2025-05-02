from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_no_login_interaction():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/customer-interaction")
        time.sleep(2)
        assert "Login" in driver.title
        print("Redirected to login page as expected.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
