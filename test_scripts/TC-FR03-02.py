
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_invalid_pro_number_filter():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://example.com/dataset")
        driver.find_element(By.ID, "filter-menu").click()
        driver.find_element(By.XPATH, "//option[text()='Contains']").click()
        driver.find_element(By.ID, "pro-number").send_keys("INVALIDPRO")
        driver.find_element(By.ID, "apply-filter").click()
        assert driver.find_element(By.CLASS_NAME, "no-results").is_displayed()
        print("No results message displayed for invalid PRO number.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
