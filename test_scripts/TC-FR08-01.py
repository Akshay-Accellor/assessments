
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_fallback_response():
 driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
 try:
 driver.get("http://maya-platform-url.com/chat")
 driver.find_element(By.ID, "chatInput").send_keys("What is cloud computing?")
 driver.find_element(By.ID, "sendBtn").click()
 time.sleep(2)
 assert "This query does not match any known company policy" in driver.page_source
 print("Received fallback response for irrelevant query.")
 finally:
 driver.quit()
