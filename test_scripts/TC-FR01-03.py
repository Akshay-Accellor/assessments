
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_sso_stay_signed_in():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://example.com/dashboard")
        driver.find_element(By.XPATH, "//button[contains(text(), 'Logout')]").click()
        print("User logged out.")
        driver.get("https://example.com/dashboard")
        assert driver.find_element(By.XPATH, "//input[@value='Yes']").is_displayed()
        driver.find_element(By.XPATH, "//input[@value='Yes']").click()
        assert driver.current_url == "https://example.com/dashboard"
        print("User logged back in successfully.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
