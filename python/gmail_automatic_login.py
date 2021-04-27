from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.google.com/intl/es-419/gmail/about/')

#x = driver.find_elements_by_class_name('h-c-header__nav-li-link')
link = driver.find_element_by_link_text('Acceder')

#print(x)
#x[0].click()
link.click()

