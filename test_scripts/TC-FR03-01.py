
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def filter_by_pro_number(url, pro_number):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "filter_button"))
        ).click()
        time.sleep(2)
        driver.find_element(By.ID, "filter_criteria").send_keys('Contains')
        driver.find_element(By.ID, "pro_number").send_keys(pro_number)
        driver.find_element(By.ID, "apply_filter").click()
        time.sleep(3)
        assert "Results containing 12345" in driver.page_source
        print("Filtering by PRO Number successful.")
    except Exception as e:
        print(f"PRO Number filtering failed: {e}")
    finally:
        driver.quit()
