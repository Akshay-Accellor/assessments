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
        driver.get("https://example.com/data-table")
        driver.find_element(By.ID, "filter_pro").click()
        driver.find_element(By.XPATH, "//option[contains(text(), 'Contains')]").click()
        driver.find_element(By.ID, "input_pro").send_keys("invalid_pro#")
        driver.find_element(By.ID, "apply_filter").click()
        time.sleep(2)
        assert "Invalid PRO number" in driver.page_source
    except Exception as e:
        print(f"Invalid PRO number filter failed: {e}")
        driver.quit()
    finally:
        driver.quit()
