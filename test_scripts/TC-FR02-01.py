
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
            EC.presence_of_element_located((By.ID, "start_date"))
        ).send_keys(start_date)
        driver.find_element(By.ID, "end_date").send_keys(end_date)
        driver.find_element(By.ID, "apply_filter").click()
        time.sleep(3)
        assert "Filtered results" in driver.page_source
        print("Data filtered successfully by date range.")
    except Exception as e:
        print(f"Filtering by date failed: {e}")
    finally:
        driver.quit()
