from selenium import webdriver

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://geta-client-webapp-dev.azurewebsites.net/#/landing')

def test_answer():
    assert driver.title == 'GETA Club Play - Genesys'
