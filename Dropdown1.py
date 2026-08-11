from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
login_url = 'https://the-internet.herokuapp.com/dropdown'
driver.get(login_url)

dropdown_element = driver.find_element(By.ID, value='dropdown')
target_value = 'Option 2'
select = Select(dropdown_element)
for option in select.options:
    if option.text == target_value:
        option.click()
        print(f"Selected option is {target_value}")
        break
    else:
        print(f"Option  '{target_value}' not found in dropdown")

#How to interact with dropdown
#How to use select class
#How to use 3 different methods
#Select by vsiable text
#Select by value
#Select by index
#How to count the dropdown values
#loop the dropdown values and if the desired value found select that value



# dropdown_element = driver.find_element(By.ID, value='dropdown')
# select = Select(dropdown_element)
# option_count = len(select.options)
#
# expected_count = 3
# if option_count == expected_count:
#     print('Test cases passed. Count is correct')
# else:
#     print('Test cases failed. Count is incorrect')


#Select the value by visible text
# select.select_by_visible_text('Option 2')

#Select the value by index
# select.select_by_index(2)

#Select the option by using a value
# select.select_by_value('1')