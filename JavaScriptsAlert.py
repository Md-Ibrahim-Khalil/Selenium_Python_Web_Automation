from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = webdriver.Firefox()
url = "https://the-internet.herokuapp.com/javascript_alerts"
browser.get(url)

# AlertButton = browser.find_element(By.XPATH, "//button[normalize-space()='Click for JS Alert']")
AlertButton = browser.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']")

AlertButton.click()
alert = browser.switch_to.alert
alert_Text = alert.text
print(alert_Text)

time.sleep(10)
# alert.accept()
alert.send_keys("This is selenium with python")
alert.accept()
# alert.dismiss()
time.sleep(10)