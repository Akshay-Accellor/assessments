
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
    driver.get("http://interaction_platform_url")
    chatbox = driver.find_element(By.ID, "chatbox")
    chatbox.send_keys("Hello, how can I help you?")
    driver.find_element(By.ID, "send_button").click()
    assert "Hello, how can I help you?" in driver.page_source
    print("Message sent successfully.")
except Exception as e:
    print(f"Error: {e}")
finally:
    driver.quit()