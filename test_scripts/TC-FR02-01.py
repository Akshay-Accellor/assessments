from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_customer_needs_survey():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/customer-needs")
        assert "Customer Needs Assessment" in driver.title
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "needs_survey"))).send_keys("Looking for affordable options")
        driver.find_element(By.ID, "submit_survey").click()
        confirmation_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "confirmation"))).text
        assert "Your needs have been recorded." in confirmation_message
        print("Test Passed: Customer needs successfully submitted.")
    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()
