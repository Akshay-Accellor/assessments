
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_incomplete_goal_data():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://yourplatform.com/goals")
        driver.find_element(By.ID, "goal_name").send_keys("Increase Sales")
        driver.find_element(By.ID, "save_goal").click()
        assert "Target is required" in driver.page_source
        print("Handled missing target input correctly.")
    finally:
        driver.quit()