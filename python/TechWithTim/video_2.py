from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://www.google.com')
print(driver.title)

search = driver.find_element_by_name('q')
search.send_keys('Youngermaster')
search.send_keys(Keys.ENTER)

# print(driver.page_source) # Prints all the page source code.