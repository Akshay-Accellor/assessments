
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import time
 
def test_inactive_interaction_button():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://customer-interaction-platform.com")
        assert "Customer Interaction" in driver.title
        driver.find_element(By.XPATH, "//button[text()='Start Interaction'][@disabled]").click()
        assert not driver.find_element(By.ID, "interaction_form").is_displayed()
        print("Negative test case passed. No action taken on inactive button.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
