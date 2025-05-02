from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_identify_customer_needs():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get('http://platform-url/customer-needs')
        driver.find_element(By.ID, 'customer_data_id').send_keys('Customer Data')
        driver.find_element(By.ID, 'analyze_button_id').click()
        assert driver.find_element(By.ID, 'trends_display_id').is_displayed() == True
        print("Customer needs identified accurately.")
    finally:
        driver.quit()
