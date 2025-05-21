
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# Test for identifying needs features
def test_identify_needs_features():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/needs-identification")
        assert driver.find_element(By.ID, "surveyOption").is_displayed()
        assert driver.find_element(By.ID, "feedbackFormOption").is_displayed()
        print("Identifying needs features test passed")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
