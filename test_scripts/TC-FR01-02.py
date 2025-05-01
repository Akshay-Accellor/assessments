from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
    driver.get("http://example.com/customer-interaction")
    assert driver.current_url == "http://example.com/login"  # Redirect to login
    assert driver.find_element(By.ID, "login-form").is_displayed()  # Login form is present
    print("Successfully redirected to the login page.")
finally:
    driver.quit()
