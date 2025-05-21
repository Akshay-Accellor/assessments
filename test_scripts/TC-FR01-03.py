
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def test_message_length_exceed():
 driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
 try:
 driver.get("http://example.com/login")
 driver.find_element(By.ID, "username").send_keys("testuser")
 driver.find_element(By.ID, "password").send_keys("testpass")
 driver.find_element(By.ID, "login_btn").click()
 WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "interaction_page"))).click()
 # Sending a long message
 long_message = "A" * 501  # 501 characters
 driver.find_element(By.ID, "message_input").send_keys(long_message)
 driver.find_element(By.ID, "send_btn").click()
 time.sleep(2)
 # Verify error message
 assert driver.find_element(By.ID, "message_length_error").is_displayed()
 print("Test case passed: Message length exceeded limit and error shown.")
 finally:
 driver.quit()
