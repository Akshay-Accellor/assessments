from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_multiple_interactions():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://example.com/login")
    # Assuming login steps here
    driver.get("http://example.com/customer-interaction")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "start_interaction_A"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "start_interaction_B"))).click()
    assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "interaction_interface_A"))) and WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "interaction_interface_B")))
    print("Test Passed: Multiple customer interactions are handled.")
    driver.quit()
