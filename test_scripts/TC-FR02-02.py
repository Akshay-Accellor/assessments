
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
 
def test_no_customer_selected():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://customer-needs-identifier.com")
        assert "Customer Needs" in driver.title
        driver.find_element(By.ID, "needs_button").click()
        assert "Please select a customer" in driver.page_source
        print("Negative test case passed. Error message displayed.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
