
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_invalid_customer_data():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://yourplatform.com/needs-identification")
        driver.find_element(By.ID, "customer_data").send_keys("@!#$%@")
        driver.find_element(By.ID, "identify_button").click()
        assert "Invalid data" in driver.page_source
        print("Invalid data error handled correctly.")
    finally:
        driver.quit()