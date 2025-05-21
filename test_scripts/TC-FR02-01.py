
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_identify_customer_needs():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://customer-needs-identification-tool.com")
        assert "Customer Needs" in driver.title
        input_element = driver.find_element(By.ID, "needsInput")
        assert input_element.is_displayed()
        input_element.send_keys("Quality Service")
        select_button = driver.find_element(By.ID, "selectButton")
        select_button.click()
        confirmation = driver.find_element(By.ID, "confirmationMessage")
        assert confirmation.is_displayed()
    finally:
        driver.quit()
