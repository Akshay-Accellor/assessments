
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def filter_invalid_pro_number(url, pro_number):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[contains(text(),'Filter PRO Number')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//select[@id='filter-criteria']").click()
        driver.find_element(By.XPATH, "//option[contains(text(), 'Contains')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='pro-number']").send_keys(pro_number)
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(text(),'Apply')]").click()
        time.sleep(3)
        error_msg = driver.find_element(By.XPATH, "//div[contains(text(), 'No matching records')]")
        assert error_msg.is_displayed()
        print("No matching records message displayed as expected.")
    except Exception as e:
        print(f"Filtering failed: {e}")
        driver.quit()
    finally:
        driver.quit()
filter_invalid_pro_number("http://example.com/dataset", "INVALID_PRO123")