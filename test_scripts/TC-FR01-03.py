from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from concurrent.futures import ThreadPoolExecutor
import time
def test_platform_max_user_load():
def open_connection(user_id):
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://customer-interaction-platform.com")
time.sleep(2)
driver.quit()
with ThreadPoolExecutor(max_workers=100) as executor:
for i in range(100):
executor.submit(open_connection, i)
