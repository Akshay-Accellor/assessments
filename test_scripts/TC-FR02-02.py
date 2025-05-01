from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
    driver.get("http://example.com/needs-identification")
    driver.find_element(By.ID, "needs-form").send_keys("a" * 256)  # Exceeding character limit
    driver.find_element(By.ID, "submit-button").click()
    time.sleep(2)
    assert "Invalid input" in driver.page_source  # Check error message
    print("Handled invalid input as expected.")
finally:
    driver.quit()
