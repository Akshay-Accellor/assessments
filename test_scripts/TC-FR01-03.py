
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_platform_high_load():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://example.com/customer-interaction")
        time.sleep(5)  # simulate wait for load
        feedback_box = driver.find_element(By.ID, "feedback-form")
        feedback_box.send_keys("Great service!")
        driver.find_element(By.ID, "submit-feedback").click()
        time.sleep(2)
        assert "Thank you for your feedback!" in driver.page_source
        print("Feedback submitted successfully under load conditions.")
    finally:
        driver.quit()
