
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
    driver.get('http://example.com/home')
    time.sleep(2)
    driver.find_element(By.ID, 'needsAssessment').click()
    time.sleep(2)
    assert driver.find_element(By.ID, 'assessmentQuestions').is_displayed() == True
finally:
    driver.quit()