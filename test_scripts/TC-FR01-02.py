
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
# Test for unable to interact without log-in
def test_no_login_interaction():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/customer-interaction")
        driver.find_element(By.ID, "chatOption").click()
        time.sleep(2)
        error_message = driver.find_element(By.ID, "error").text
        assert "Please log in to interact" in error_message
        print("No login interaction test passed")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
