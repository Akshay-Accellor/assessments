
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_filter_by_pro_number():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://example.com/dataset")
        driver.find_element(By.ID, "filter-menu").click()
        driver.find_element(By.XPATH, "//option[text()='Contains']").click()
        driver.find_element(By.ID, "pro-number").send_keys("PRO123456")
        driver.find_element(By.ID, "apply-filter").click()
        assert "PRO123456" in driver.page_source
        print("Filtered results displayed correctly.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
