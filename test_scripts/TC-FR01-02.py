from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_no_access_to_interaction_platform():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get('http://yourapp.com/interact')
        time.sleep(2)
        assert driver.current_url == 'http://yourapp.com/login'  # Check redirect to login
        assert "Please log in to access this feature" in driver.page_source  # Check warning message
    finally:
        driver.quit()
