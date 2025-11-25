
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_missing_analysis_data():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://yourplatform.com/market-analysis")
        driver.find_element(By.ID, "analyze_button").click()
        assert "Data required" in driver.page_source
        print("Correctly prompts for input in market analysis.")
    finally:
        driver.quit()