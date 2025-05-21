
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
# Test for platform load time
def test_platform_load_time():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        start_time = time.time()
        driver.get("http://example.com/customer-interaction")
        load_time = time.time() - start_time
        assert load_time < 5
        print("Load time test passed")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
