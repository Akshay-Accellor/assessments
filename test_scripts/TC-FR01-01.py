
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_customer_interaction_platform():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://customer-interaction-platform.com")
        assert "Welcome" in driver.title
        chat_feature = driver.find_element(By.ID, "chatFeature")
        assert chat_feature.is_displayed()
    finally:
        driver.quit()
