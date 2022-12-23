from selenium import webdriver

browser = webdriver.Chrome()
# selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH.
# Please see https://chromedriver.chromium.org/home
browser.quit()

browser = webdriver.Firefox()
# selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH.
# 'geckodriver' executable needs to be in PATH.
# Please see https://github.com/mozilla/geckodriver/releases
browser.get('http://eddypagan.com')
elem = browser.find_element_by_css_selector('body > div.wp-site-blocks > div > div > div > div > div:nth-child(2) > a')
elem.click()

browser.get('http://google.com')
search_elem = browser.find_element_by_css_selector('body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf.emcav > div.RNNXgb > div > div.a4bIc > input')
search_elem.send_keys('Eddy Pagan')
search_elem.submit()

browser.back()
browser.forward()
browser.refresh()
browser.quit()
