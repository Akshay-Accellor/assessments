
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def apply_invalid_date_filter(url, start_date, end_date):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        driver.find_element(By.XPATH, "//input[@id='start-date']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='start-date']").send_keys(start_date)
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='end-date']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='end-date']").send_keys(end_date)
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Apply Filter')]").click()
        error_message = driver.find_element(By.ID, "error-message").text
        assert error_message == "Invalid date", "Error message not displayed"
    finally:
        driver.quit()
