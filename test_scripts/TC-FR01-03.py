from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://maya-platform/login")
driver.find_element(By.ID, "username").send_keys("")
driver.find_element(By.ID, "password").send_keys("")
driver.find_element(By.ID, "loginBtn").click()
assert "Please enter username and password." in driver.page_source
driver.quit()
