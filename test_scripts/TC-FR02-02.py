
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_invalid_date_filter():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://example.com/data")
        driver.find_element(By.ID, "start-date").click()
        driver.find_element(By.XPATH, "//td[@data-date='2022-01-01']").click()  # Invalid start date
        assert driver.find_element(By.CLASS_NAME, "error").is_displayed()
        print("Error message displayed for invalid start date.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
