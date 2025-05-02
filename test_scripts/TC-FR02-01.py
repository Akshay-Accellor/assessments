from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_identify_customer_needs():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://example.com/customer-needs")
    assert "Customer Needs Assessment" in driver.title
    driver.find_element(By.ID, "customerDetails").send_keys("Customer A")
    driver.find_element(By.ID, "identifyNeedsBtn").click()
    assert driver.find_element(By.ID, "needsIdentified").is_displayed()
    driver.quit()
