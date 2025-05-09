from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://maya-platform/chat")
driver.find_element(By.ID, "chatBox").send_keys("What time is it?")
driver.find_element(By.ID, "sendBtn").click()
assert "This query does not match any known company policy." in driver.page_source
driver.quit()
