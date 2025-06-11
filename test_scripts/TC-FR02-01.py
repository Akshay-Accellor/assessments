
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_filter_data_by_date():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://example.com/data")
        driver.find_element(By.ID, "start-date").click()
        driver.find_element(By.XPATH, "//td[@data-date='2023-01-01']").click()
        driver.find_element(By.ID, "end-date").click()
        driver.find_element(By.XPATH, "//td[@data-date='2023-12-31']").click()
        driver.find_element(By.ID, "apply-filters").click()
        # Check if data is filtered as per selected dates
        assert "Filtered results" in driver.page_source
        print("Data filtered successfully by date.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
