from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://maya-platform/chat")
for i in range(5):
driver.find_element(By.ID, "chatBox").send_keys("What is policy question "+str(i))
driver.find_element(By.ID, "sendBtn").click()
time.sleep(1)
assert "response" in driver.page_source
driver.quit()
