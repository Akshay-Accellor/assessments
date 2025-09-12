

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def filter_by_pro_number(url, pro_number):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Filter')]").click()
        driver.find_element(By.XPATH, "//option[contains(text(), 'Contains')]").click()
        driver.find_element(By.XPATH, "//input[@id='pro-number']").send_keys(pro_number)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Apply')]").click()
        assert "Filtered results" in driver.page_source
        print("Dataset filtered by specified PRO Number.")
    except Exception as e:
        print(f"Filtering failed: {e}")
    finally:
        driver.quit()

