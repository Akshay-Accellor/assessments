
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
# Test for platform to launch interaction options
def test_platform_launch():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/customer-interaction")
        assert "Customer Interaction" in driver.title
        assert driver.find_element(By.ID, "chatOption").is_displayed()
        assert driver.find_element(By.ID, "emailOption").is_displayed()
        print("Platform launch test passed")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
