from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_pro_number_filter():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://yourapp.com/data")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'filter_button'))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "filter_criteria"))).select_by_visible_text("Contains")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "pro_number"))).send_keys("12345")
        driver.find_element(By.ID, 'apply_filter').click()
        results = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'results_table')))
        assert results.is_displayed()
        print("PRO Number filter applied, results shown.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
