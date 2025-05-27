
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_unauthorized_access():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://example.com/interaction_platform")  # Unauthorized access
    assert "Unauthorized Access" in driver.page_source
    assert not driver.find_elements(By.XPATH, "//button[text()='Chat with Us']")
    driver.quit()
