
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_empty_feedback_form():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://yourplatform.com")
        driver.find_element(By.ID, "feedback_form").submit()
        assert "This field is required" in driver.page_source
        print("Correctly prompts for input in feedback form.")
    finally:
        driver.quit()