
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
 
def test_identify_customer_needs():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://customer-needs-identifier.com")
        assert "Customer Needs" in driver.title
        driver.find_element(By.ID, "customer_select").send_keys("John Doe")
        driver.find_element(By.ID, "needs_button").click()
        assert driver.find_element(By.ID, "needs_display").is_displayed()
        print("Positive test case passed. Customer needs displayed.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
