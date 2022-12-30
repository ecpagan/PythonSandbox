from selenium import webdriver
from selenium.webdriver.common.by import By

brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

option = webdriver.ChromeOptions()
option.binary_location = brave_path

browser = webdriver.Chrome(options=option)
browser.maximize_window()
browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
assert 'Selenium Easy Demo' in browser.title
assert 'Show Message' in browser.page_source
show_message_button = browser.find_element(By.CLASS_NAME, 'btn-default')
show_message_button_text = show_message_button.get_attribute('innerHTML')

user_message = browser.find_element(By.ID, 'user-message')
user_message.clear()
test_string = 'I AM EXTRA COOOOL'
user_message.send_keys(test_string)

show_message_button.click()
output_message = browser.find_element(By.ID, 'display')
assert test_string in output_message.text

# same button but using css selector
show_message_button2 = browser.find_element(By.CSS_SELECTOR, '#get-input > .btn')

browser.quit()
