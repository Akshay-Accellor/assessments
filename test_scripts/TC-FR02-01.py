
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
    driver.get("http://needs_identification_url")
    assert "Needs Identification" in driver.title
    assert driver.find_element(By.ID, "customer_info").is_displayed()
    assert driver.find_element(By.ID, "needs_description").is_displayed()
    print("Form fields are displayed correctly.")
except Exception as e:
    print(f"Error: {e}")
finally:
    driver.quit()