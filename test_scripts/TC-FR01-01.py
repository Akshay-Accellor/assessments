
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_customer_interaction():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://yourapplicationurl.com/customer-interaction")
        assert "Customer Interaction" in driver.title

        driver.find_element(By.ID, "newInteractionButton").click()
        assert driver.find_element(By.ID, "interactionForm").is_displayed()

        driver.find_element(By.ID, "inputDetails").send_keys("Customer feedback")
        driver.find_element(By.ID, "submitButton").click()
        assert "Interaction created" in driver.page_source
        print("Test Passed: Customer interaction created")
    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()
