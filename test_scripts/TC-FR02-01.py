from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_date_filter():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://yourapp.com/filter")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'start_date'))).send_keys("01/01/2023")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'end_date'))).send_keys("01/31/2023")
        driver.find_element(By.ID, 'apply_filters').click()
        results = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'results_table')))
        assert results.is_displayed()
        print("Filters applied and results displayed successfully.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
