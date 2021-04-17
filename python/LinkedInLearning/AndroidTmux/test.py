from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument('--headless') # EN SEGUNDO PLANO, SIN GUI

driver = webdriver.Firefox(executable_path='/usr/bin/geckodriver', options=options)

driver.get('https://google.es')
html = driver.page_source
print(html)

driver.quit()