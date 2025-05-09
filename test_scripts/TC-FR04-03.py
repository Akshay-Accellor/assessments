from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://maya-platform/chat")
for i in range(10):
driver.find_element(By.ID, "chatBox").send_keys(f"Message {i}")
driver.find_element(By.ID, "sendBtn").click()
assert f"Message {i}" in driver.page_source
driver.quit()
