
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_sso_login_invalid():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://example.com/login")
        driver.find_element(By.XPATH, "//button[contains(text(), 'Login with SSO')]").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("invaliduser")
        driver.find_element(By.ID, "next").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password"))).send_keys("wrongpassword")
        driver.find_element(By.ID, "login").click()
        alert = driver.find_element(By.CLASS_NAME, "error")
        assert alert.is_displayed() and "Invalid" in alert.text
        print("Error message displayed as expected.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
