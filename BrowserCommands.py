import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()

# Open website
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(5)

# Find and click Forgot Password
driver.find_element(
    By.CSS_SELECTOR,
    ".oxd-text.oxd-text--p.orangehrm-login-forgot-header"
).click()

time.sleep(10)

# Go back
driver.back()
time.sleep(10)

# Refresh
driver.refresh()
time.sleep(30)

# Close browser
driver.quit()