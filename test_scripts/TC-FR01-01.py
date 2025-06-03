
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_customer_interaction():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get('http://yourplatform.com/login')
        # Assume login code here
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'interactionPage'))
        )
        assert 'Customer Interaction' in driver.title
        driver.find_element(By.ID, 'startInteractionBtn').click()
        assert driver.find_element(By.ID, 'selectCustomerPopup').is_displayed()
    finally:
        driver.quit()
