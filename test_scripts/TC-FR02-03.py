

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def clear_filters(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Clear Filters')]").click()
        all_data_visible = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'All data displayed')]")))
        assert all_data_visible.is_displayed()
        print("All data displayed after clearing filters.")
    except Exception as e:
        print(f"Clearing filters failed: {e}")
    finally:
        driver.quit()

