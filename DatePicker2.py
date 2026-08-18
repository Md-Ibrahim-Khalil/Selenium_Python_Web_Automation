from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime, timedelta

from selenium.webdriver.support.select import Select

browser = webdriver.Firefox()
browser.minimize_window()
url = "https://demo.automationtesting.in/Datepicker.html"
browser.get(url)
browser.find_element(By.ID, value="datepicker2").click()
time.sleep(10)
current_date = datetime.now()
print(current_date)

next_day = current_date + timedelta(days=1)
print(next_day)

Next_day = (str(next_day.day))
print(Next_day)

current_month = datetime.now().month
print(current_month)

current_year = datetime.now().year
print(current_year)

next_month = (current_month % 12) + 1
next_month_year = f"{next_month}/{current_year}"

Month_Dropdown = browser.find_element(By.CSS_SELECTOR, "select[title='Change the month']")
select = Select(Month_Dropdown)
select.select_by_value(str(next_month_year))

Year_Dropdown = browser.find_element(By.CSS_SELECTOR, "select[title='Change the year']")
select = Select(Year_Dropdown)
select.select_by_visible_text("2024")
browser.find_element(By.LINK_TEXT,Next_day).click()
time.sleep(10)