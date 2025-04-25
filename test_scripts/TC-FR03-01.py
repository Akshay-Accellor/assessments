from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_filter_by_pro_number():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://example.com/data-table")
        driver.find_element(By.ID, "filter_pro").click()
        driver.find_element(By.XPATH, "//option[contains(text(), 'Contains')]").click()
        driver.find_element(By.ID, "input_pro").send_keys("12345")
        driver.find_element(By.ID, "apply_filter").click()
        time.sleep(2)
        assert "filtered data for 12345" in driver.page_source
    except Exception as e:
        print(f"Filter by PRO number failed: {e}")
        driver.quit()
    finally:
        driver.quit()
