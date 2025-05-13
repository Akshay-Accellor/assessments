from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_no_input_needs():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/needs-identification")
        time.sleep(2)
        assert "Identify Needs" in driver.title
        driver.find_element(By.ID, "submitWithoutInput").click()
        time.sleep(2)
        assert "Please select a need" in driver.page_source
        print("Validation error displayed for no input.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
