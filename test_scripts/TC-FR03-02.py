
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_empty_credentials():
 driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
 try:
 driver.get("http://maya-platform-url.com/login")
 driver.find_element(By.ID, "loginBtn").click()
 time.sleep(2)
 assert "Please enter username" in driver.page_source
 print("Empty credentials handled correctly.")
 finally:
 driver.quit()
