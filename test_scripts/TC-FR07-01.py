from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_irrelevant_query_response():
    # Setup\n    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://maya-platform.com/chat')
    driver.find_element(By.ID, 'chat-input').send_keys('What is cloud computing?')
    driver.find_element(By.ID, 'chat-input').send_keys('\n')
    time.sleep(2)
    response = driver.find_element(By.ID, 'response-output').text
    assert 'This query does not match any known company policy' in response
    driver.quit()
