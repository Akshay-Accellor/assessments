
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
    driver.get('http://example.com')
    driver.find_element(By.XPATH, "//button[contains(text(), 'Interact with customers')]").click()
    time.sleep(2)
    assert "Could not load" in driver.page_source
finally:
    driver.quit()