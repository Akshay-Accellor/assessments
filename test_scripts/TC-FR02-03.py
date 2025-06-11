
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_reset_filters():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://example.com/data")
        driver.find_element(By.ID, "start-date").click()
        driver.find_element(By.XPATH, "//td[@data-date='2023-01-01']").click()
        driver.find_element(By.ID, "end-date").click()
        driver.find_element(By.XPATH, "//td[@data-date='2023-12-31']").click()
        driver.find_element(By.ID, "apply-filters").click()
        assert "Filtered results" in driver.page_source
        driver.find_element(By.ID, "reset-filters").click()
        # Check if all data is visible
        assert "Initial data" in driver.page_source
        print("Filters reset successfully.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
