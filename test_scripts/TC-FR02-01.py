from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_retrieve_customer_needs():
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
driver.get("http://customer-interaction-platform.com")
# Assuming user login happens here
assert driver.find_element(By.ID, "customer-needs-section").is_displayed()
needs_data = driver.find_element(By.ID, "customer-needs").text
assert needs_data != "", "No customer needs data found"
finally:
driver.quit()
