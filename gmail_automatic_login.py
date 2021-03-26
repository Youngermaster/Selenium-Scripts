from selenium import webdriver

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://www.google.com/intl/es-419/gmail/about/')

#x = driver.find_elements_by_class_name('h-c-header__nav-li-link')
link = driver.find_element_by_link_text('Acceder')

#print(x)
#x[0].click()
link.click()

