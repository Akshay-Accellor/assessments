
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
    driver.get('http://example.com/platform')
    assert driver.find_element(By.XPATH, "//button[contains(text(), 'Chat')]").is_displayed()
    assert driver.find_element(By.XPATH, "//button[contains(text(), 'Email')]").is_displayed()
    assert driver.find_element(By.XPATH, "//button[contains(text(), 'Call')]").is_displayed()
finally:
    driver.quit()