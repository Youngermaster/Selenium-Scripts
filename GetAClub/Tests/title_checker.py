from selenium import webdriver

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://geta-client-webapp-dev.azurewebsites.net/#/landing')
#print(driver.title)
if driver.title == 'GETA Club Play - Genesys':
    print('[Success]')
else:
    print('[Error]')