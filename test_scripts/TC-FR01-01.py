from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_platform_load_time():
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
driver.get("http://customer-interaction-platform.com")
start_time = time.time()
# Wait for the page to fully load
time.sleep(3)
end_time = time.time()
load_time = end_time - start_time
assert load_time < 3, f"Load time exceeded: {load_time} seconds"
finally:
driver.quit()
