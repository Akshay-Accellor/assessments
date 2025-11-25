
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_extreme_goal_values():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://yourplatform.com/goals")
        driver.find_element(By.ID, "goal_name").send_keys("Grow Company to New Heights")
        driver.find_element(By.ID, "goal_target").send_keys("500%")
        driver.find_element(By.ID, "save_goal").click()
        assert "Goal saved" in driver.page_source
        print("Extreme goal values processed successfully.")
    finally:
        driver.quit()