from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_needs_identification_tool():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get('http://example.com/needs')
        assert "Needs Identification" in driver.title
        driver.find_element(By.ID, 'customer_name').send_keys('Test User')
        driver.find_element(By.ID, 'submit').click()
        assert "Needs Identified" in driver.page_source
        print("Needs identification tool functions correctly.")
    finally:
        driver.quit()
