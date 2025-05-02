from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_invalid_customer_id():
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
driver.get("http://customer-interaction-platform.com")
# Assuming user login happens here
assert driver.find_element(By.ID, "customer-needs-section").is_displayed()
driver.find_element(By.ID, "customer-id-input").send_keys("invalid_id")
driver.find_element(By.ID, "search-button").click()
assert "Invalid customer ID" in driver.page_source
finally:
driver.quit()
