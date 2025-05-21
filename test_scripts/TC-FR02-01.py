
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def test_needs_identification():
 driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
 try:
 driver.get("http://example.com/login")
 driver.find_element(By.ID, "username").send_keys("testuser")
 driver.find_element(By.ID, "password").send_keys("testpass")
 driver.find_element(By.ID, "login_btn").click()
 WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "needs_tool"))).click()
 # Fill in customer details
 driver.find_element(By.ID, "customer_name").send_keys("John Doe")
 driver.find_element(By.ID, "customer_needs").send_keys("Feedback on services")
 driver.find_element(By.ID, "save_btn").click()
 time.sleep(2)
 # Verify needs report
 assert driver.find_element(By.ID, "needs_report").is_displayed()
 print("Test case passed: Needs report generated.")
 finally:
 driver.quit()
