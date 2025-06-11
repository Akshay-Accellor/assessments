
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def sso_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("URL")
        driver.find_element(By.XPATH, "//button[contains(text(), 'Login with SSO')]").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "i0116"))).send_keys("testuser")
        driver.find_element(By.ID, "idSIButton9").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "i0118"))).send_keys("Password123")
        driver.find_element(By.ID, "idSIButton9").click()
        print("Login successful.")
    except Exception as e:
        print(f"Failed to login: {e}")
    finally:
        driver.quit()
