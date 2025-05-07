from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_response_format():
    # Setup\n    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://maya-platform.com/chat')
    driver.find_element(By.ID, 'chat-input').send_keys('What are the travel guidelines?')
    driver.find_element(By.ID, 'chat-input').send_keys('\n')
    time.sleep(2)
    response = driver.find_element(By.ID, 'response-output').text
    assert len(response) > 0  # Ensure some response is shown
    driver.quit()
