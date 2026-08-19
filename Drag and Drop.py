import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.maximize_window()

browser.get("https://the-internet.herokuapp.com/drag_and_drop")
print(browser.current_url)

time.sleep(3)

source_element = browser.find_element(By.ID, "column-a")
destination_element = browser.find_element(By.ID, "column-b")

actions = ActionChains(browser)

actions.click_and_hold(source_element)
actions.move_to_element(destination_element)
actions.release()
actions.perform()
time.sleep(5)
browser.quit()

browser.quit()