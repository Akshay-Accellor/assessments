from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_platform_no_internet():
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
driver.get("http://customer-interaction-platform.com")
assert "No connection" in driver.page_source
finally:
driver.quit()
