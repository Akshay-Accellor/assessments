
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_interaction_platform():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://yourplatform.com")
        assert 'Welcome' in driver.title
        assert driver.find_element(By.ID, "chatbox").is_displayed()
        assert driver.find_element(By.ID, "feedback_form").is_displayed()
        print("Platform loaded successfully with elements.")
    finally:
        driver.quit()