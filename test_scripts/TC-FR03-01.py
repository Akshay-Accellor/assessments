
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def filter_pro_number_valid():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("URL")
        driver.find_element(By.ID, "filter_menu").click()
        driver.find_element(By.XPATH, "//select[@id='filter_criteria']/option[text()='Contains']").click()
        driver.find_element(By.ID, "pro_number_input").send_keys("12345")
        driver.find_element(By.ID, "apply_pro_filters").click()
        assert "filtered results" in driver.page_source
    except Exception as e:
        print(f"Filtering by PRO Number failed: {e}")
    finally:
        driver.quit()
