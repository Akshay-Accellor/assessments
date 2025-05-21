
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
    driver.find_element(By.ID, "submit_button").click()
    assert "Required fields must be filled" in driver.page_source
    print("Error message displayed for incomplete form.")
except Exception as e:
    print(f"Error: {e}")
finally:
    driver.quit()