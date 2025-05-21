
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# Test for no input submission
def test_no_input_identification():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/needs-identification")
        driver.find_element(By.ID, "submitButton").click()
        time.sleep(2)
        error_message = driver.find_element(By.ID, "error").text
        assert "Please fill in all fields" in error_message
        print("No input test passed")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
