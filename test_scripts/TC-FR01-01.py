
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def test_customer_interaction():
 driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
 try:
 driver.get("http://example.com/login")
 # User logs in
 driver.find_element(By.ID, "username").send_keys("testuser")
 driver.find_element(By.ID, "password").send_keys("testpass")
 driver.find_element(By.ID, "login_btn").click()
 WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "interaction_page"))).click()
 # Sending a message
 driver.find_element(By.ID, "message_input").send_keys("Hello Customer!")
 driver.find_element(By.ID, "send_btn").click()
 time.sleep(2)
 # Verify message sent
 assert driver.find_element(By.ID, "success_message").is_displayed()
 print("Test case passed: Message sent successfully.")
 finally:
 driver.quit()
