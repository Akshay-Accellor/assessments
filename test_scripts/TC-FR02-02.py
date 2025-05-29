
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_authentication_invalid_session():
 driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
 try:
 driver.get("http://maya-platform-url.com/login")
 driver.find_element(By.ID, "username").send_keys("validUser")
 driver.find_element(By.ID, "password").send_keys("randomToken")
 driver.find_element(By.ID, "loginBtn").click()
 time.sleep(2)
 assert "Login" in driver.title
 print("Remained on login page with invalid session.")
 finally:
 driver.quit()
