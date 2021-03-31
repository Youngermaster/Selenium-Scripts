from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait 

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASSWORD')

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

url = 'https://forms.office.com/Pages/ResponsePage.aspx?id=XrX3mb6ce0aBQ5GXgpGK-2xPFY02OMtHi8uuteRYEGxUME9PUE1BSkRZREkzUDBGM1dBWjhRVFEyNS4u'

driver.get(url)
input_email = driver.find_element_by_xpath('/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/input[1]')
input_email.clear()
input_email.send_keys(EMAIL)
input_email.send_keys(Keys.RETURN)

input_password = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath('/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/input'))
input_password.clear()
input_password.send_keys(PASSWORD)
input_password.send_keys(Keys.RETURN)

button_stay_signed = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath('/html/body/div/form/div/div/div[1]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div[1]/input'))
button_stay_signed.click()


form_first_question = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath('/html/body/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/label/input'))
form_first_question.click()