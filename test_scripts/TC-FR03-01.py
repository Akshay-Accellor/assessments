
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_show_error_message():
 driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
 try:
 driver.get("http://maya-platform-url.com/login")
 driver.find_element(By.ID, "username").send_keys("wrongUser")
 driver.find_element(By.ID, "password").send_keys("wrongPass")
 driver.find_element(By.ID, "loginBtn").click()
 time.sleep(2)
 assert "Invalid username or password" in driver.page_source
 print("Error message displayed correctly.")
 finally:
 driver.quit()
