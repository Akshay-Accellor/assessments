
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def sso_login(url, username, password):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        # Click on SSO login button
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login with SSO')]"))).click()
        time.sleep(2)
        # Enter username
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "username_field"))).send_keys(username)
        # Enter password
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "password_field"))).send_keys(password)
        driver.find_element(By.ID, "submit_button").click()
        WebDriverWait(driver, 10).until(EC.title_contains("Dashboard"))
        print("Login successful and redirected to Dashboard.")
    except Exception as e:
        print(f"Login failed: {e}")
    finally:
        driver.quit()
