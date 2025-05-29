
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_query_posh_act():
 driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
 try:
 driver.get("http://maya-platform-url.com/chat")
 driver.find_element(By.ID, "chatInput").send_keys("What is the POSH Act?")
 driver.find_element(By.ID, "sendBtn").click()
 time.sleep(2)
 assert "The POSH Act" in driver.page_source
 print("Correct response received for POSH Act.")
 finally:
 driver.quit()
