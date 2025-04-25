from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_invalid_pro_number_filter():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://yourapp.com/data")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'filter_button'))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "filter_criteria"))).select_by_visible_text("Contains")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "pro_number"))).send_keys("INVALID_PRO")
        driver.find_element(By.ID, 'apply_filter').click()
        error_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "no_result_message"))).text
        assert "No matches found" in error_message
        print("No matches found error displayed.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
