
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
 
def test_rapid_clicks():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://customer-interaction-platform.com")
        assert "Customer Interaction" in driver.title
        button = driver.find_element(By.XPATH, "//button[text()='Start Interaction']")
        for _ in range(10):
            button.click()
            time.sleep(0.1)
        assert driver.find_element(By.ID, "interaction_form").is_displayed()
        print("Edge test case passed. Interaction form displayed.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
