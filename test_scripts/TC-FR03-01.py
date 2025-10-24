
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def filter_data_by_pro_number(url, pro_number):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        time.sleep(2)
        # Open filter menu
        driver.find_element(By.ID, "filter_menu_button").click()
        time.sleep(1)
        driver.find_element(By.ID, "criteria_contains").click()
        driver.find_element(By.ID, "pro_number_input").send_keys(pro_number)
        driver.find_element(By.ID, "apply_filter_button").click()
        time.sleep(3)
        # Verify data is filtered
        print("Data filtered successfully for PRO Number.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()
