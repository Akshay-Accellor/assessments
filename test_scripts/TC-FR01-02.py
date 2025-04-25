from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#function for the login functionality
def test_sso_invalid_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://yourapp.com/login")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login with SSO')]"))
        ).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username_field"))).send_keys("invalid_user@example.com")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password_field"))).send_keys("invalid_password")
        driver.find_element(By.ID, "login_button").click()
        error_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "error_message"))).text
        assert "Invalid username or password" in error_message
        print("Error message displayed successfully.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
