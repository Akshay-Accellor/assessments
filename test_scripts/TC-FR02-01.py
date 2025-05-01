from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
    driver.get("http://example.com/needs-identification")
    driver.find_element(By.ID, "needs-form").send_keys("I need help with billing.")
    driver.find_element(By.ID, "submit-button").click()
    time.sleep(2)
    assert "Your needs have been recorded." in driver.page_source  # Check confirmation message
    print("Needs identified and submitted.")
finally:
    driver.quit()
