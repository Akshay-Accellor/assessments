from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_blank_fields_required():
    # Setup\n    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://maya-platform.com/login')
    driver.find_element(By.ID, 'login-btn').click()
    assert 'Please fill in this field' in driver.page_source
    driver.quit()
