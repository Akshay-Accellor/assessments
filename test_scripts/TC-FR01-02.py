
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def sso_login_invalid():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("URL")
        driver.find_element(By.XPATH, "//button[contains(text(), 'Login with SSO')]").click()
        driver.find_element(By.ID, "i0116").send_keys("wronguser")
        driver.find_element(By.ID, "idSIButton9").click()
        driver.find_element(By.ID, "i0118").send_keys("wrongpassword")
        driver.find_element(By.ID, "idSIButton9").click()
        assert "error message" in driver.page_source
    except Exception as e:
        print(f"Login failed: {e}")
    finally:
        driver.quit()
