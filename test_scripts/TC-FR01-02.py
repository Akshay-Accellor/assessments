
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException
import time
try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://interaction_platform_url")
    assert "ERR_INTERNET_DISCONNECTED" in driver.page_source
    print("Error message displayed due to no internet.")
except WebDriverException:
    print("Platform not reachable as expected.")
finally:
    driver.quit()