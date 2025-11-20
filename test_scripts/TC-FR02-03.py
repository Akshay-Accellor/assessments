
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
            EC.presence_of_element_located((By.ID, "clear_filters"))
        ).click()
        time.sleep(3)
        assert "All records" in driver.page_source
        print("Filters cleared successfully, all records are displayed.")
    except Exception as e:
        print(f"Failed to clear filters: {e}")
    finally:
        driver.quit()
