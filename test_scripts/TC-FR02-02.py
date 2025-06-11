
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def filter_by_date_invalid():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("URL")
        driver.find_element(By.ID, "start_date").click()
        driver.find_element(By.XPATH, "//td[contains(@class, 'day') and text()='10']").click()
        driver.find_element(By.ID, "end_date").click()
        driver.find_element(By.XPATH, "//td[contains(@class, 'day') and text()='1']").click()
        assert "error message" in driver.page_source
        driver.find_element(By.ID, "apply_filters").click()
        assert "no results" in driver.page_source
    except Exception as e:
        print(f"Filtering failed: {e}")
    finally:
        driver.quit()
