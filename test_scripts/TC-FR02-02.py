
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_invalid_data():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/identify-needs")
        driver.find_element(By.ID, "customerData").send_keys("Invalid Data")
        driver.find_element(By.ID, "identifyButton").click()
        assert "Invalid data" in driver.page_source
        print("Invalid Data Test Passed")
    except Exception as e:
        print(f"Error during invalid data test: {e}")
    finally:
        driver.quit()
