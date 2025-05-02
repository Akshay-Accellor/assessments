from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_invalid_data_analysis():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get('http://platform-url/customer-needs')
        driver.find_element(By.ID, 'customer_data_id').send_keys('')
        driver.find_element(By.ID, 'analyze_button_id').click()
        assert driver.find_element(By.ID, 'error_message_id').is_displayed() == True
        print("Error message displayed for invalid data input.")
    finally:
        driver.quit()
