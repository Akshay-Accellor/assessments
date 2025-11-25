
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_open_market_analysis():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://yourplatform.com/market-analysis")
        assert driver.find_element(By.ID, "analyze_button").is_displayed()
        driver.find_element(By.ID, "analyze_button").click()
        assert driver.find_element(By.ID, "analysis_window").is_displayed()
        print("Market analysis window opened successfully.")
    finally:
        driver.quit()