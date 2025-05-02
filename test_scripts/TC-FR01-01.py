from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_customer_interaction_portal():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/customer-interaction")
        assert "Customer Interaction" in driver.title
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "start_interaction"))).click()
        assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "interaction_interface")))
        print("Test Passed: Access to interaction platform verified.")
    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()
