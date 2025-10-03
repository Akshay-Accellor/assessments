
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def apply_date_filter(url, start_date, end_date):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='start-date']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, f"//td[@data-date='{start_date}']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='end-date']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, f"//td[@data-date='{end_date}']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(text(),'Apply')]").click()
        time.sleep(3)
        assert "Filtered" in driver.page_source
        print("Date filter applied successfully.")
    except Exception as e:
        print(f"Filter application failed: {e}")
        driver.quit()
    finally:
        driver.quit()
apply_date_filter("http://example.com/data", "2023-01-01", "2023-01-31")