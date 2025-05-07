from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_empty_login():
    # Setup\n    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://maya-platform.com/login')
    # Step 1: Leave username blank
    # Step 2: Leave password blank
    # Step 3: Click login
    driver.find_element(By.ID, 'login-btn').click()
    # Assertion
    error_messages = [driver.find_element(By.ID, 'username').get_attribute('validationMessage'), driver.find_element(By.ID, 'password').get_attribute('validationMessage')]
    assert all(error == 'Please fill in this field.' for error in error_messages)
    driver.quit()
