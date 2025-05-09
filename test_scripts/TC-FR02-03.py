from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://maya-platform/chat")
start_time = time.time()
driver.find_element(By.ID, "chatBox").send_keys("How to get a quote?")
driver.find_element(By.ID, "sendBtn").click()
response_time = time.time() - start_time
assert response_time < 2
driver.quit()
