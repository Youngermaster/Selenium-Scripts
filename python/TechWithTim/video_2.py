from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://www.google.com')
print(driver.title)

search = driver.find_element_by_name('q')
search.send_keys('Youngermaster')
search.send_keys(Keys.ENTER)

print(driver.page_source)