from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_valid_login():
    # Setup\n    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://maya-platform.com/login')
    # Step 1: Input username
    driver.find_element(By.ID, 'username').send_keys('validUser')
    # Step 2: Input password
    driver.find_element(By.ID, 'password').send_keys('validPassword')
    # Step 3: Click login
    driver.find_element(By.ID, 'login-btn').click()
    # Assertion
    assert 'dashboard' in driver.current_url
    driver.quit()
