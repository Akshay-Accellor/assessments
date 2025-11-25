
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_create_content():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://yourplatform.com/create-content")
        driver.find_element(By.ID, "content_title").send_keys("New Marketing Strategy")
        driver.find_element(By.ID, "content_body").send_keys("Description of strategy...")
        driver.find_element(By.ID, "create_content").click()
        assert "Content created" in driver.page_source
        print("Content creation successful.")
    finally:
        driver.quit()