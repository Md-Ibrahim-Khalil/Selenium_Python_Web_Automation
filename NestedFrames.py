from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.maximize_window()
browser.get('https://the-internet.herokuapp.com/nested_frames')

#Switch to top frame
browser.switch_to.frame('frame-top')
#Switch to Middle frame
browser.switch_to.frame('frame-middle')

content = browser.find_element(By.ID, 'content').text
print("Content in middle frame", content)

#Switch to default content
browser.switch_to.default_content()

#Switch to bottom frame
browser.switch_to.frame('frame-bottom')
content_bottom = browser.find_element(By.TAG_NAME, 'body').text
print("Content in bottom frame", content_bottom)