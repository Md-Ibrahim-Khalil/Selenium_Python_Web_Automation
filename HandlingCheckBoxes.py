import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get("https://fs8.formsite.com/IpfhfE/5fx0retdop/index")
browser.maximize_window()
time.sleep(10)
browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
checkboxes = browser.find_elements(By.XPATH,value="//input[@type='checkbox']")
for checkbox in checkboxes:
    checkbox.send_keys(Keys.SPACE)

checked_count = 0
for checkbox in checkboxes:
    if checkbox.is_selected():
        checked_count +=1

expected_checked_count = 11
if checked_count == expected_checked_count:
    print("Checkbox count verified")
else:
    print("Checkbox count not verified")

time.sleep(10)
browser.quit()