from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_interaction_without_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://example.com/customer-interaction")
    assert "Login" in driver.title
    driver.quit()
