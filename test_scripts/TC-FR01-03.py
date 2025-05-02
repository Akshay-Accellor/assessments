from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_high_load():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get('http://example.com/interaction')
        start_time = time.time()
        for _ in range(100):
            # Simulate user interaction
            driver.find_element(By.ID, 'chat_box').send_keys('Hello')
        end_time = time.time()
        assert (end_time - start_time) < 2
        print("Platform remains responsive under load.")
    finally:
        driver.quit()
