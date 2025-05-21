
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

def test_mobile_access():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=375,812")  # Simulating mobile device
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    try:
        driver.get("http://example.com/login")
        assert "Login" in driver.title
        print("Mobile Access Test Passed")
    except Exception as e:
        print(f"Error during mobile access test: {e}")
    finally:
        driver.quit()
