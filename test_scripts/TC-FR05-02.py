
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_no_data_source():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://yourplatform.com/data-gathering")
        driver.find_element(By.ID, "gather_data").click()
        assert "Data source required" in driver.page_source
        print("Handled missing data source correctly.")
    finally:
        driver.quit()