from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def filter_data_by_date(url, start_date, end_date):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "startDatePicker"))
        ).click()
        time.sleep(1)
        driver.find_element(By.XPATH, f"//td[@data-date='{start_date}']").click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "endDatePicker"))
        ).click()
        time.sleep(1)
        driver.find_element(By.XPATH, f"//td[@data-date='{end_date}']").click()
        driver.find_element(By.ID, 'filterButton').click()
        print("Data filtered based on date range.")
    except Exception as e:
        print(f"Filtering failed: {e}")
    finally:
        driver.quit()
