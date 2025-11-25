
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_no_internet():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://yourplatform.com")
        time.sleep(5)
        assert "No Internet" in driver.page_source
        print("Error message displayed for no internet.")
    finally:
        driver.quit()