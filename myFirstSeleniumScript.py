from selenium import webdriver

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://www.google.com')

#Simple assignment
#from selenium.webdriver import Firefox

#driver = Firefox()
#driver.get('https://www.google.com')
#Or use the context manager
#from selenium.webdriver import Firefox

#with Firefox() as driver:
   #your code inside this indent
#   driver.get('https://www.google.com')