from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_chat_responsiveness():
    # Setup\n    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://maya-platform.com/chat')
    # Step 1: Check chat readiness
    assert driver.find_element(By.ID, 'chat-input').is_displayed()
    input_field = driver.find_element(By.ID, 'chat-input')
    input_field.send_keys('Hello')
    # Step 2: Verify sending message
    ActionChains(driver).send_keys('\n').perform()  # Sending the message
    # Further checks could go here
    driver.quit()
