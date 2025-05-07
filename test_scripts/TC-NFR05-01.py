from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_no_errors_on_invalid_query():
    # Setup\n    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://maya-platform.com/chat')
    driver.find_element(By.ID, 'chat-input').send_keys('Invalid question')
    driver.find_element(By.ID, 'chat-input').send_keys('\n')
    time.sleep(2)
    assert 'does not match any known company policy' in driver.page_source
    driver.quit()
