from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_chat_interface_access():
    # Setup\n    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://maya-platform.com/chat')
    # Step 1: Access chat interface
    assert driver.title == 'Chat Interface'  # Title may vary
    assert driver.find_element(By.ID, 'chat-input').is_displayed()
    driver.quit()
