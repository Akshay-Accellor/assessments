from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_access_needs_identification():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get('http://yourapp.com')
        driver.find_element(By.ID, 'customer-needs-button').click()  # Click button
        time.sleep(2)
        assert driver.find_element(By.ID, 'needs-interface').is_displayed()  # Check if needs interface is displayed
        print("Needs identification interface verified")
    finally:
        driver.quit()
