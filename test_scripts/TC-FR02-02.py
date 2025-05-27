
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_incomplete_assessment():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://example.com/login")
    driver.find_element(By.ID, "username").send_keys("testuser")
    driver.find_element(By.ID, "password").send_keys("Pass123!")
    driver.find_element(By.ID, "loginBtn").click()
    driver.get("http://example.com/needs_assessment")
    driver.find_element(By.ID, "submitBtn").click()
    assert "Please complete all required fields" in driver.page_source
    driver.quit()
