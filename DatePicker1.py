import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.maximize_window()

url = "https://demoqa.com/date-picker"
browser.get(url)

time.sleep(3)

# Find date input
date_picker = browser.find_element(
    By.ID,
    "datePickerMonthYearInput"
)

# Click date input
date_picker.click()

time.sleep(2)

# Get today's date
current_date = datetime.datetime.now()

# Get tomorrow's date
next_date = current_date + datetime.timedelta(days=1)

# Convert date to string
formatted_date = next_date.strftime("%m/%d/%Y")

# Select existing date
date_picker.send_keys(Keys.COMMAND, "a")

# Enter tomorrow's date
date_picker.send_keys(formatted_date)

# Press TAB
date_picker.send_keys(Keys.TAB)

time.sleep(5)

browser.quit()