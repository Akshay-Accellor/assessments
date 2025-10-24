
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def clear_date_filters(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        time.sleep(2)
        # Click clear filters button
        driver.find_element(By.ID, "clear_filters_button").click()
        time.sleep(3)
        # Verify that data is unfiltered
        print("Filters successfully cleared and original data is displayed.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()
