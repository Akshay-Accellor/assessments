from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_access_customer_platform_not_logged_in():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://yourappurl.com")
        time.sleep(2)
        driver.find_element(By.ID, "customersTab").click()
        time.sleep(1)
        assert "Login" in driver.title  # Ensure login page is displayed
        print("Redirected to login page as expected.")
    finally:
        driver.quit()