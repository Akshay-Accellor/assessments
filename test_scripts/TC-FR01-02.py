from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_invalid_customer_input():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get('http://platform-url/interaction')
        driver.find_element(By.ID, 'customer_input_id').send_keys('Invalid Data')
        driver.find_element(By.ID, 'submit_button_id').click()
        error_message = driver.find_element(By.ID, 'error_message_id').is_displayed()
        assert error_message == True
        print("Error message displayed for invalid input.")
    finally:
        driver.quit()
