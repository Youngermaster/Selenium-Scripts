from selenium import webdriver
from selenium.webdriver.common.by import By

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://geta-client-webapp-dev.azurewebsites.net/#/landing')

button = driver.find_element_by_xpath('/html/body/genesys-root/genesys-landing-page/section/div/div/div/swiper/div/div[1]/div[2]/div/div[3]/button[1]')
button.click()