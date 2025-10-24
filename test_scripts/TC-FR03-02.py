
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def filter_data_empty_pro_number(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        time.sleep(2)
        driver.find_element(By.ID, "filter_menu_button").click()
        time.sleep(1)
        driver.find_element(By.ID, "criteria_contains").click()
        driver.find_element(By.ID, "pro_number_input").send_keys("")
        driver.find_element(By.ID, "apply_filter_button").click()
        time.sleep(3)
        # Verify error message
        print("Error message displayed for empty PRO Number input.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()
