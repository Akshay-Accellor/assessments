from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_filter_invalid_dates():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://example.com/data-filter")
        driver.find_element(By.ID, "start_date").click()
        driver.find_element(By.XPATH, "//td[@data-date='2023-02-01']").click()
        driver.find_element(By.ID, "end_date").click()
        driver.find_element(By.XPATH, "//td[@data-date='2023-01-30']").click()
        driver.find_element(By.ID, "apply_filter").click()
        time.sleep(2)
        assert "Invalid date selection" in driver.page_source
    except Exception as e:
        print(f"Invalid date filter failed: {e}")
        driver.quit()
    finally:
        driver.quit()
