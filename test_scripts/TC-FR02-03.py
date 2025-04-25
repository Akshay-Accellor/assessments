from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_clear_filters():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://example.com/data-filter")
        driver.find_element(By.ID, "clear_filter").click()
        time.sleep(2)
        assert "original data" in driver.page_source
    except Exception as e:
        print(f"Clear filters failed: {e}")
        driver.quit()
    finally:
        driver.quit()
