
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def apply_date_filter(url, start_date, end_date):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        driver.find_element(By.XPATH, "//input[@id='start-date']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, f"//td[contains(@data-date, '{start_date}')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='end-date']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, f"//td[contains(@data-date, '{end_date}')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Apply Filter')]").click()
        print("Filter applied successfully.")
    finally:
        driver.quit()
