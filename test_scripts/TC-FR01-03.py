
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import threading
import time

def access_interaction_platform():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://example.com/interaction_platform")
    assert driver.find_element(By.XPATH, "//button[text()='Chat with Us']").is_displayed()
    driver.quit()

def test_high_load():
    threads = [threading.Thread(target=access_interaction_platform) for _ in range(100)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print("Test completed successfully for high load.")
