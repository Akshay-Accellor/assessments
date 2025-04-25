from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def filter_data_by_pro(url, pro_number):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'filterButton'))
        ).click()
        time.sleep(1)
        driver.find_element(By.ID, 'filterType').send_keys('Contains')
        driver.find_element(By.ID, 'proNumberInput').send_keys(pro_number)
        driver.find_element(By.ID, 'applyFilters').click()
        print("Data filtered based on PRO Number.")
    except Exception as e:
        print(f"Filtering by PRO Number failed: {e}")
    finally:
        driver.quit()
