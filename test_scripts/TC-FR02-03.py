
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def clear_date_filter(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Clear Filters')]").click()
        time.sleep(2)
        start_date_value = driver.find_element(By.ID, "start-date").get_attribute("value")
        end_date_value = driver.find_element(By.ID, "end-date").get_attribute("value")
        assert start_date_value == "" and end_date_value == "", "Fields are not cleared"
        print("Filters cleared successfully.")
    finally:
        driver.quit()
