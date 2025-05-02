from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_invalid_submission():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/customer-needs")
        assert "Customer Needs Assessment" in driver.title
        driver.find_element(By.ID, "needs_survey").send_keys("")  # Empty response
        driver.find_element(By.ID, "submit_survey").click()
        error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "error_message"))).text
        assert "This field is required." in error_message
        print("Test Passed: Submission correctly fails for invalid input.")
    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()
