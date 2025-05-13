from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_non_existent_user_interaction():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/login")
        time.sleep(2)
        driver.find_element(By.ID, "username").send_keys("nonexistentuser")
        driver.find_element(By.ID, "password").send_keys("Password123")
        driver.find_element(By.ID, "loginButton").click()
        time.sleep(2)
        assert "User does not exist" in driver.page_source
        print("Appropriate error message displayed for non-existent user.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
