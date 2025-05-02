from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_high_load_interaction():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get('http://platform-url/interaction')
        start_time = time.time()
        for _ in range(100):
            driver.find_element(By.ID, 'customer_input_id').send_keys('Customer Data')
            driver.find_element(By.ID, 'submit_button_id').click()
        end_time = time.time()
        assert (end_time - start_time) < 2,
        print("System maintains performance under load.")
    finally:
        driver.quit()
