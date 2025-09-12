

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def filter_no_results(url, invalid_pro_number):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Filter')]").click()
        driver.find_element(By.XPATH, "//option[contains(text(), 'Contains')]").click()
        driver.find_element(By.XPATH, "//input[@id='pro-number']").send_keys(invalid_pro_number)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Apply')]").click()
        no_results_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'No results found')]")))
        assert no_results_message.is_displayed()
        print("No results message displayed correctly.")
    except Exception as e:
        print(f"Filtering failed: {e}")
    finally:
        driver.quit()

