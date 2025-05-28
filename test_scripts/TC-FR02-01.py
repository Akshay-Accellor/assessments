
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
    driver.get('http://example.com/customer-needs')
    assert "Needs Assessment" in driver.title
    needs_input = driver.find_element(By.ID, "needs")
    needs_input.send_keys("Need assistance with product selection")
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)
    assert "Thank you for your input" in driver.page_source
finally:
    driver.quit()