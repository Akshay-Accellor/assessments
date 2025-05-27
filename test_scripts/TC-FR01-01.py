
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_interaction_platform():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://example.com")  # replace with actual URL
    assert "Home" in driver.title
    driver.find_element(By.XPATH, "//a[text()='Interaction Platform']").click()
    assert "Interaction Platform" in driver.title
    assert driver.find_element(By.XPATH, "//button[text()='Chat with Us']").is_displayed()
    driver.find_element(By.XPATH, "//button[text()='Chat with Us']").click()
    time.sleep(2)
