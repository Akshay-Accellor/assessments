from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import threading
import time
def test_access_interaction_platform():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/customer-interaction")
        assert "Customer Interaction" in driver.title  # Check title
        print("User accessed successfully.")
    finally:
        driver.quit()
threads = []
for i in range(5):
    thread = threading.Thread(target=test_access_interaction_platform)
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
