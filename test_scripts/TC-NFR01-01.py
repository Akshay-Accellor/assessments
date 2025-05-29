
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_chat_interface_responsiveness():
 driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
 try:
 driver.get("http://maya-platform-url.com/chat")
 driver.find_element(By.ID, "chatInput").send_keys("Hello, is this working?")
 driver.find_element(By.ID, "sendBtn").click()
 time.sleep(2)
 assert "Hello" in driver.page_source
 print("Chat interface is responsive.")
 finally:
 driver.quit()
