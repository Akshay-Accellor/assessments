
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def apply_pro_filter(url, pro_number):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Filter')]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//select[@id='criteria']").select_by_visible_text("Contains")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='pro-number']").send_keys(pro_number)
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Apply Filter')]").click()
        print("PRO filter applied successfully.")
    finally:
        driver.quit()
