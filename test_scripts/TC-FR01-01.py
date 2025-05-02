from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_platform_load():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get('http://platform-url')
        assert 'Platform Title' in driver.title
        # Check for interaction features
        interaction_present = driver.find_element(By.ID, 'interaction_features_id').is_displayed()
        assert interaction_present == True
        print("Platform loaded with interaction features.")
    finally:
        driver.quit()
