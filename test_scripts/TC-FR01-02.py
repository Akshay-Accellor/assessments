
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_platform_load_failure():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://example.com/invalid-url")
        time.sleep(2)
        assert "404 Not Found" in driver.page_source
        print("Correctly handled invalid URL.")
    except TimeoutException:
        print("Page failed to load within timeout.")
    finally:
        driver.quit()
