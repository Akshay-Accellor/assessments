
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_customer_interaction_without_login():
 driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
 try:
 driver.get("http://example.com/interaction")
 time.sleep(2)
 # Verify that the user is redirected to the login page
 assert "login" in driver.current_url
 # Attempt to send a message
 driver.find_element(By.ID, "send_btn").click()
 time.sleep(2)
 # Verify error message
 assert driver.find_element(By.ID, "login_required_message").is_displayed()
 print("Test case passed: System prompts user to log in.")
 finally:
 driver.quit()
