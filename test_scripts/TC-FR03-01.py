from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_invalid_login_message():
    # Setup\n    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://maya-platform.com/login')
    driver.find_element(By.ID, 'username').send_keys('fakeUser')
    driver.find_element(By.ID, 'password').send_keys('wrongPass')
    driver.find_element(By.ID, 'login-btn').click()
    # Assertion
    error_message = driver.find_element(By.ID, 'error-msg').text
    assert error_message == 'Invalid username or password'
    driver.quit()
