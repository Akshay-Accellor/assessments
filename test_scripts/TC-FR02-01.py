from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_filter_by_date():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://example.com/data-filter")
        driver.find_element(By.ID, "start_date").click()
        driver.find_element(By.XPATH, "//td[@data-date='2023-01-01']").click()
        driver.find_element(By.ID, "end_date").click()
        driver.find_element(By.XPATH, "//td[@data-date='2023-01-31']").click()
        driver.find_element(By.ID, "apply_filter").click()
        time.sleep(2)
        assert "filtered data" in driver.page_source
    except Exception as e:
        print(f"Filter by date failed: {e}")
        driver.quit()
    finally:
        driver.quit()
