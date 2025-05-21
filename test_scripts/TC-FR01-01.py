
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_platform_load():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://example.com/customer-interaction")
        time.sleep(2)
        assert "Customer Interaction" in driver.title
        assert driver.find_element(By.ID, "chat-widget").is_displayed()
        assert driver.find_element(By.ID, "feedback-form").is_displayed()
        print("Customer interaction platform loaded successfully.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
