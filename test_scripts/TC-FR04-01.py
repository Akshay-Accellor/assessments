
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_chat_interface():
 driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
 try:
 driver.get("http://maya-platform-url.com/chat")
 assert driver.find_element(By.ID, "chatInput").is_displayed()
 assert driver.find_element(By.ID, "sendBtn").is_displayed()
 print("Chat interface is loaded and ready.")
 finally:
 driver.quit()
