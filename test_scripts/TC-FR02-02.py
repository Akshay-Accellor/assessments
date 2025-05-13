from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_incomplete_customer_data():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get('http://example.com/needs')
        driver.find_element(By.ID, 'customer_name').send_keys('')
        driver.find_element(By.ID, 'submit').click()
        assert "This field is required" in driver.page_source
        print("Error message displayed correctly for incomplete data.")
    finally:
        driver.quit()
