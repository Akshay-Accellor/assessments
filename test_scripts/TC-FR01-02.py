
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_chat_interaction():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://customer-interaction-platform.com")
        driver.find_element(By.ID, "chatFeature").click()
        message_box = driver.find_element(By.ID, "messageBox")
        message_box.send_keys("Hello")
        driver.find_element(By.ID, "sendButton").click()
        confirmation = driver.find_element(By.ID, "confirmationMessage")
        assert confirmation.is_displayed()
    finally:
        driver.quit()
