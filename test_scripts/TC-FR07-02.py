
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_missing_content_fields():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://yourplatform.com/create-content")
        driver.find_element(By.ID, "create_content").click()
        assert "Title and content are required" in driver.page_source
        print("Handled missing fields correctly.")
    finally:
        driver.quit()