from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://maya-platform/chat")
driver.set_window_size(800, 600)
assert driver.find_element(By.ID, "chatBox").is_displayed()
assert driver.find_element(By.ID, "sendBtn").is_enabled()
driver.quit()
