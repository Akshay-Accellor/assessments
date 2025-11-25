
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_data_gathering_tool():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://yourplatform.com/data-gathering")
        driver.find_element(By.ID, "gather_data").click()
        assert "Gathering in progress" in driver.page_source
        print("Data gathering initiated successfully.")
    finally:
        driver.quit()