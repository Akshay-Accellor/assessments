
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
 
def test_customer_interaction_platform():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://customer-interaction-platform.com")
        assert "Customer Interaction" in driver.title
        driver.find_element(By.XPATH, "//button[text()='Start Interaction']").click()
        assert driver.find_element(By.ID, "interaction_form").is_displayed()
        feedback_input = driver.find_element(By.ID, "feedback")
        feedback_input.send_keys("Great service!")
        assert feedback_input.get_attribute("value") == "Great service!"
        print("Positive test case passed.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
