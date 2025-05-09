from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def clear_date_filters(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'clearButton'))
        ).click()
        original_data_present = driver.find_element(By.ID, 'defaultDataID').is_displayed()
        assert original_data_present, "Original data view is not displayed after clearing filters."
        print("Filters cleared successfully and original data is shown.")
    except Exception as e:
        print(f"Error occurred while clearing filters: {e}")
    finally:
        driver.quit()
