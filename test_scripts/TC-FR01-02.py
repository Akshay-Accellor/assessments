from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_invalid_url():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get('http://example.com/invalid')
        assert "404 Not Found" in driver.page_source
        print("Error message displayed correctly for invalid URL.")
    finally:
        driver.quit()
