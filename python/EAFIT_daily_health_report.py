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

driver = webdriver.Chrome()

url = 'https://forms.office.com/Pages/ResponsePage.aspx?id=XrX3mb6ce0aBQ5GXgpGK-2xPFY02OMtHi8uuteRYEGxUME9PUE1BSkRZREkzUDBGM1dBWjhRVFEyNS4u'

driver.get(url)
# input_email = driver.find_element_by_name('loginfmt')
input_email = WebDriverWait(driver, 10).until(
    lambda x: x.find_element_by_name('loginfmt'))
input_email.clear()
input_email.send_keys(EMAIL)
input_email.send_keys(Keys.RETURN)

input_password = WebDriverWait(driver, 10).until(
    lambda x: x.find_element_by_name('passwd'))
input_password.clear()
input_password.send_keys(PASSWORD)
input_password.send_keys(Keys.RETURN)


button_stay_signed = WebDriverWait(driver, 10).until(
    lambda x: x.find_element_by_id('idSIButton9'))
button_stay_signed.click()

form_first_question = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(
    '/html/body/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/label/span/span'))
form_first_question.click()

form_second_question = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(
    '//html/body/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/label/input'))
form_second_question.click()

form_third_question = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(
    '/html/body/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div[3]/div/div[2]/div/div[2]/div/label/input'))
form_third_question.click()

form_fourth_question = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(
    '/html/body/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[2]/div/label/input'))
form_fourth_question.click()

form_fith_question = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(
    '/html/body/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div[5]/div/div[2]/div/div[2]/div/label/input'))
form_fith_question.click()

form_sixth_question = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(
    '/html/body/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div[6]/div/div[2]/div/div[2]/div/label/input'))
form_sixth_question.click()

form_seventh_question = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(
    '/html/body/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div[7]/div/div[2]/div/div[2]/div/label/input'))
form_seventh_question.click()

submit = driver.find_element_by_class_name('button-content')
submit.click()
