
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def test_invalid_needs_identification():
 driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
 try:
 driver.get("http://example.com/login")
 driver.find_element(By.ID, "username").send_keys("testuser")
 driver.find_element(By.ID, "password").send_keys("testpass")
 driver.find_element(By.ID, "login_btn").click()
 WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "needs_tool"))).click()
 # Try saving without filling details
 driver.find_element(By.ID, "save_btn").click()
 time.sleep(2)
 # Verify error message
 assert driver.find_element(By.ID, "error_message").is_displayed()
 print("Test case passed: System shows error for invalid input.")
 finally:
 driver.quit()
