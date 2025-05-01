from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
    driver.get("http://example.com/customer-interaction")
    assert "Customer Interaction" in driver.title
    assert driver.find_element(By.XPATH, "//h1[text()='Customer Interaction']").is_displayed()  # Header is visible
    assert driver.find_element(By.ID, "send-message-button").is_displayed()  # Button is present
    print("Successfully accessed the customer interaction platform.")
finally:
    driver.quit()
