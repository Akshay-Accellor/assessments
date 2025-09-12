

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def apply_date_filters(url, start_date, end_date):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "start-date-picker"))).send_keys(start_date)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "end-date-picker"))).send_keys(end_date)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Apply Filters')]").click()
        assert "Data updated" in driver.page_source
        print("Data filtered by selected dates.")
    except Exception as e:
        print(f"Filtering failed: {e}")
    finally:
        driver.quit()

