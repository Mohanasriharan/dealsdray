
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By

chrome_options = ChromeOptions()

username="prexo.mis@dealsdray.com"
password="prexo.mis@dealsdray.com"

url=("https://demo.dealsdray.com/")

driver = webdriver.Chrome(options=chrome_options)

driver.get(url)

driver.find_element(By.NAME,"username").send_keys(username)
driver.find_element(By.NAME,"password").send_keys(password)
driver.find_element(By.XPATH, "//button[@type='submit']").click()

print("logged")
sleep(5)

driver.find_element(By.XPATH, "//button[@type='button']").click()
driver.get("https://demo.dealsdray.com/")







