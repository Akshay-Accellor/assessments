from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_customer_interaction():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://example.com/login")
    # Login process
    driver.find_element(By.ID, "username").send_keys("valid_user")
    driver.find_element(By.ID, "password").send_keys("valid_pass")
    driver.find_element(By.ID, "loginBtn").click()
    time.sleep(2)
    # Navigate to customer interaction page
    driver.get("http://example.com/customer-interaction")
    assert "Customer Interaction" in driver.title
    # Select customer
    driver.find_element(By.ID, "selectCustomer").click()
    assert driver.find_element(By.ID, "customerDetails").is_displayed()
    # Send message
    driver.find_element(By.ID, "messageInput").send_keys("Hello!")
    driver.find_element(By.ID, "sendMessageBtn").click()
    assert driver.find_element(By.ID, "confirmationMessage").is_displayed()
    driver.quit()
