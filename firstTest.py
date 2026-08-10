from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://selenium.dev/")
driver.maximize_window()
title = driver.title
print(title)
assert "Selenium" in title

element = driver.findElement(By.xpath("#APjFqb"))

