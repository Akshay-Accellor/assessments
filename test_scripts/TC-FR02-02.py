
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
    driver.get('http://example.com/home')
    driver.find_element(By.ID, 'logoutButton').click()
    time.sleep(2)
    driver.get('http://example.com/needsAssessment')
    time.sleep(2)
    assert "Please log in to continue" in driver.page_source
finally:
    driver.quit()