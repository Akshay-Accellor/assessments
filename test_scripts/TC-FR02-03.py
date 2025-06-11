
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def clear_filters():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("URL")
        driver.find_element(By.ID, "start_date").click()
        driver.find_element(By.XPATH, "//td[contains(@class, 'day') and text()='1']").click()
        driver.find_element(By.ID, "end_date").click()
        driver.find_element(By.XPATH, "//td[contains(@class, 'day') and text()='31']").click()
        driver.find_element(By.ID, "apply_filters").click()
        driver.find_element(By.ID, "clear_filters").click()
        assert "original data" in driver.page_source
    except Exception as e:
        print(f"Clearing filters failed: {e}")
    finally:
        driver.quit()
