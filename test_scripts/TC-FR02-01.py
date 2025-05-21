
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_identify_needs():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/identify-needs")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "customerData"))).send_keys("Sample Customer Data")
        driver.find_element(By.ID, "identifyButton").click()
        assert "Needs Report" in driver.page_source
        print("Identify Needs Test Passed")
    except Exception as e:
        print(f"Error during needs identification: {e}")
    finally:
        driver.quit()
