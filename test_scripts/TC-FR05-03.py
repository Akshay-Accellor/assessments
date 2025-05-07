from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_policy_query_code_of_conduct():
    # Setup\n    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://maya-platform.com/chat')
    driver.find_element(By.ID, 'chat-input').send_keys('What is the code of conduct policy?')
    driver.find_element(By.ID, 'chat-input').send_keys('\n')
    time.sleep(2)
    response = driver.find_element(By.ID, 'response-output').text
    assert 'code of conduct' in response
    driver.quit()
