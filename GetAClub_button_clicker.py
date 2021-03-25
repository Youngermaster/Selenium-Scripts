from selenium import webdriver

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://getaclub.io')

x = driver.find_elements_by_class_name('close')
link = driver.find_element_by_link_text('ABOUT US')

print(x)
x[0].click()
link.click()
