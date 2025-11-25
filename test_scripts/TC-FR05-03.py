
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_large_data_set_gathering():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://yourplatform.com/data-gathering")
        driver.find_element(By.ID, "data_upload").send_keys("/path/to/large_data_file.csv")
        driver.find_element(By.ID, "gather_data").click()
        assert "Completed gathering" in driver.page_source
        print("Successfully processed large data file.")
    finally:
        driver.quit()