from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://maya-platform/chat")
driver.find_element(By.ID, "chatBox").send_keys("What is the health insurance policy?")
driver.find_element(By.ID, "sendBtn").click()
assert "Our health insurance policy covers..." in driver.page_source
driver.quit()
