
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def clear_date_filter(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[contains(text(),'Clear filters')]").click()
        time.sleep(3)
        assert "All Records" in driver.page_source
        print("Filters were cleared successfully.")
    except Exception as e:
        print(f"Clearing filters failed: {e}")
        driver.quit()
    finally:
        driver.quit()
clear_date_filter("http://example.com/data")