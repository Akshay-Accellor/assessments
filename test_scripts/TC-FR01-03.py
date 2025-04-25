from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_sso_multi_step_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://yourapp.com/login")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login with SSO')]"))
        ).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username_field"))).send_keys("user@example.com")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password_field"))).send_keys("password123")
        driver.find_element(By.ID, "login_button").click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='No']"))).click()
        WebDriverWait(driver, 10).until(EC.url_contains("/dashboard"))
        assert "Dashboard" in driver.title
        print("Login successful without 'Stay signed in'.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
