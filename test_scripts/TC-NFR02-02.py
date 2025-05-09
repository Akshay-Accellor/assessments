from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://maya-platform/chat")
queries = ["What is maternity leave?","What is sick leave?"]
for query in queries:
driver.find_element(By.ID, "chatBox").send_keys(query)
driver.find_element(By.ID, "sendBtn").click()
assert "The maternity leave policy states..." in driver.page_source
driver.quit()
