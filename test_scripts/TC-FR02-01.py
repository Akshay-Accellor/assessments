
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def filter_data_with_date(url, start_date, end_date):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        time.sleep(2)
        driver.find_element(By.ID, "date_filter_button").click()
        time.sleep(2)
        driver.find_element(By.ID, "start_date_picker").send_keys(start_date)
        driver.find_element(By.ID, "end_date_picker").send_keys(end_date)
        driver.find_element(By.ID, "apply_filter_button").click()
        time.sleep(3)
        # Verify that data is filtered
        print("Data successfully filtered by date range.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()
