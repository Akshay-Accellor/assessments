from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_no_customers_available():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://example.com/login")
    # Simulating no customers
    driver.find_element(By.ID, "username").send_keys("valid_user")
    driver.find_element(By.ID, "password").send_keys("valid_pass")
    driver.find_element(By.ID, "loginBtn").click()
    time.sleep(2)
    driver.get("http://example.com/customer-interaction")
    assert driver.find_element(By.ID, "noCustomersMessage").is_displayed()
    driver.quit()
