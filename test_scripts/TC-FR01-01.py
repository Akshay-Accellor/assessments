from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_start_interaction():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/customer-interaction")
        time.sleep(2)
        assert "Customer Interaction" in driver.title
        driver.find_element(By.ID, "startInteractionButton").click()
        time.sleep(2)
        assert driver.find_element(By.ID, "interactionInterface").is_displayed()
        print("Interaction started successfully.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
