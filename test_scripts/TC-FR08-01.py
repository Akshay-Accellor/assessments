from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_fallback_response_irrelevant_query():
    # Setup\n    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://maya-platform.com/chat')
    driver.find_element(By.ID, 'chat-input').send_keys('What is cloud computing?')
    driver.find_element(By.ID, 'chat-input').send_keys('\n')
    time.sleep(2)
    response = driver.find_element(By.ID, 'response-output').text
    assert 'Please refer to our HR or documentation' in response
    driver.quit()
