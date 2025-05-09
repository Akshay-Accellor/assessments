from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://maya-platform/chat")
driver.find_element(By.ID, "chatBox").send_keys("Can I get details about vacation policy?")
driver.find_element(By.ID, "sendBtn").click()
response = driver.page_source
assert "Our vacation policy states..." in response
driver.quit()
