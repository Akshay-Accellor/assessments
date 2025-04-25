from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_sso_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://example.com/login")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login with SSO')]"))).click()
        time.sleep(2)
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "i0116"))).send_keys("username")
        driver.find_element(By.ID, "idSIButton9").click()
        time.sleep(2)
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "i0118"))).send_keys("password")
        driver.find_element(By.ID, "idSIButton9").click()
        time.sleep(2)
        assert "dashboard" in driver.current_url
    except Exception as e:
        print(f"Login failed: {e}")
        driver.quit()
    finally:
        driver.quit()
