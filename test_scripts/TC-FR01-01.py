
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
    assert "Interaction Platform" in driver.title
    assert driver.find_element(By.ID, "chatbox").is_displayed()
    assert driver.find_element(By.ID, "feedback_form").is_displayed()
    print("Platform elements are displayed.")
except Exception as e:
    print(f"Error: {e}")
finally:
    driver.quit()