from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_authentication_process():
    # Setup\n    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://maya-platform.com/login')
    driver.find_element(By.ID, 'username').send_keys('validUser')
    driver.find_element(By.ID, 'password').send_keys('validPassword')
    driver.find_element(By.ID, 'login-btn').click()
    assert 'dashboard' in driver.current_url
    driver.quit()
