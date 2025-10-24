
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def sso_login_persistent(url, username, password):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Login with SSO')]").click()
        time.sleep(2)
        driver.find_element(By.ID, "i0116").send_keys(username)
        driver.find_element(By.ID, "idSIButton9").click()
        time.sleep(2)
        driver.find_element(By.ID, "i0118").send_keys(password)
        driver.find_element(By.ID, "idSIButton9").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@value='Yes']").click()
        print("Login successful with persistent choice.")
    finally:
        driver.quit()
