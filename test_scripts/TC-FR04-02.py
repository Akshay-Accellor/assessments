
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_chat_interface_access_without_login():
 driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
 try:
 driver.get("http://maya-platform-url.com/chat")
 time.sleep(2)
 assert "Login" in driver.title
 print("Redirected to login page without access to chat.")
 finally:
 driver.quit()
