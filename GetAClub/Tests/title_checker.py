from selenium import webdriver
import platform

driver = None
if platform.system() == 'Windows':
    PATH = 'C:\Program Files (x86)\chromedriver.exe'
    driver = webdriver.Chrome(PATH)
elif platform.system() == 'Linux':
    PATH = 'drivers/chromedriver'
    driver = webdriver.Chrome(PATH)
else:
    print("[ERROR]")

driver.get('https://geta-client-webapp-dev.azurewebsites.net/#/landing')

def test_answer():
    assert driver.title == 'GETA Club Play - Genesys'
