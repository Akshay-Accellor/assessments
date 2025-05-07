from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_chat_responsiveness():
    # Setup\n    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://maya-platform.com/chat')
    driver.find_element(By.ID, 'chat-input').send_keys('Hello, world!')
    driver.find_element(By.ID, 'chat-input').send_keys('\n')
    assert 'Hello, world!' in driver.page_source
    driver.quit()
