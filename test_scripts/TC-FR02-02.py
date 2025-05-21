
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_no_input_identification():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://customer-needs-identification-tool.com")
        driver.find_element(By.ID, "identifyButton").click()
        error_message = driver.find_element(By.ID, "errorMessage")
        assert error_message.is_displayed()
    finally:
        driver.quit()
