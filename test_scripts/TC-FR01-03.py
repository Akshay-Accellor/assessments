
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
    driver.get('http://example.com/home')
    driver.find_element(By.ID, 'customerInteraction').click()
    time.sleep(2)
    guest_options = driver.find_elements(By.CLASS_NAME, 'guestOption')
    loggedin_options = driver.find_elements(By.CLASS_NAME, 'userOption')
    assert len(guest_options) < len(loggedin_options)
finally:
    driver.quit()