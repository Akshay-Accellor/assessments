
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_identify_customer_needs():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://example.com/customer-needs-assessment")
        time.sleep(2)
        driver.find_element(By.ID, "question1").send_keys("I need better support.")
        driver.find_element(By.ID, "question2").send_keys("More product options.")
        driver.find_element(By.ID, "submit-needs").click()
        time.sleep(2)
        assert "Needs identified successfully" in driver.page_source
        print("Customer needs identified without issue.")
    finally:
        driver.quit()
