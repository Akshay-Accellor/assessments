
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_customer_interaction(url, username, password):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        # Login
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login"))).send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login_button").click()

        # Navigate to interaction page
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "customer_interaction"))).click()
        assert driver.find_element(By.ID, "new_interaction").is_displayed()

        # Fill in the interaction details
        driver.find_element(By.ID, "new_interaction").click()
        driver.find_element(By.ID, "interaction_details").send_keys("Discuss product features.")
        driver.find_element(By.ID, "submit_button").click()
        # Validate confirmation message
        assert "Interaction submitted successfully." in driver.page_source
        print("Test completed successfully.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
