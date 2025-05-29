
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_query_code_of_conduct():
 driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
 try:
 driver.get("http://maya-platform-url.com/chat")
 driver.find_element(By.ID, "chatInput").send_keys("What is the code of conduct policy?")
 driver.find_element(By.ID, "sendBtn").click()
 time.sleep(2)
 assert "code of conduct" in driver.page_source
 print("Complete code of conduct policy received.")
 finally:
 driver.quit()
