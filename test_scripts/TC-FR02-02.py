
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
    driver.get('http://example.com/customer-needs')
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)
    assert "Field cannot be empty" in driver.page_source
finally:
    driver.quit()