from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()
browser.maximize_window()
browser.get('https://autotest.how/demo/tinymce/')

tinymce = browser.find_element(By.ID, 'tinymce_ifr')
browser.switch_to.frame(tinymce)

Text_Editor = browser.find_element(By.ID, value='tinymce')
Text_Editor.clear()
Text_Editor.send_keys('This is an amazing text')
time.sleep(10)

browser.switch_to.default_content()
Selenium_link = browser.find_element(By.XPATH, value="//a[@aria-label='Build with TinyMCE']")
Selenium_link.click()
