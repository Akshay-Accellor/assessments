from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_interaction_platform():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get('http://example.com/interaction')
        assert "Customer Interaction" in driver.title
        assert driver.find_element(By.ID, 'chat_box').is_displayed()
        print("Interaction platform loads successfully.")
    finally:
        driver.quit()
