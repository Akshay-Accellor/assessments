from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_no_access_without_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/customer-interaction")
        assert "Login" in driver.title
        error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "error_message"))).text
        assert "Access denied" in error_message
        print("Test Passed: Access denied error shown for non-logged users.")
    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()
