
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_invalid_market_research_parameters():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://yourplatform.com/market-research")
        driver.find_element(By.ID, "research_parameters").send_keys("!!!")
        driver.find_element(By.ID, "start_research").click()
        assert "Invalid parameters" in driver.page_source
        print("Handled invalid parameters correctly.")
    finally:
        driver.quit()