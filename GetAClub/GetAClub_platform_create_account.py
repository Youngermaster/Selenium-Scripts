from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait 
# Imports a random password generator
from generate_password import generate_password_with_special_characters

# Use pip install names
import names

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://geta-client-webapp-dev.azurewebsites.net/#/landing')

# WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath())
signup_button = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath('/html/body/genesys-root/genesys-landing-page/section/div/div/div/swiper/div/div[1]/div[2]/div/div[3]/button[1]'))
signup_button.click()

date_selector = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath('/html/body/genesys-root/genesys-signup-page/section/div/div/div/form/div/div[1]/input'))
date_selector.click()

first_calendar_period = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_class('mat-calendar-period-button')) 
first_calendar_period.click()

previous_arrow_button = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath('/html/body/div[3]/div[2]/div/mat-dialog-container/mat-datepicker-content/mat-calendar/mat-calendar-header/div/div/button[2]')) 
previous_arrow_button.click()

year_selector = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/mat-dialog-container/mat-datepicker-content/mat-calendar/div/mat-multi-year-view/table/tbody/tr[3]/td[2]/div[1]')
year_selector.click()

month_selector = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/mat-dialog-container/mat-datepicker-content/mat-calendar/div/mat-year-view/table/tbody/tr[2]/td[3]/div[1]')
month_selector.click()

day_selector = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/mat-dialog-container/mat-datepicker-content/mat-calendar/div/mat-month-view/table/tbody/tr[4]/td[2]/div[1]')
day_selector.click()

submit_date = driver.find_element_by_xpath('/html/body/genesys-root/genesys-signup-page/section/div/div[2]/div/form/div/div[2]/button')
submit_date.click()

# name = names.get_last_name()
# email = name + '@gmail.com'
# password = generate_password_with_special_characters(10) + 'a'
# 
# file = open("emailsAndPasswords.txt", "a")
# file.write("________________\n")
# file.write(f"\nName: {name}")
# file.write(f"\nEmail: {email}")
# file.write(f"\nPassword: {password}\n")
# file.write("________________\n")
# file.close()
# 
# 
# full_name_input = driver.find_element_by_xpath('/html/body/genesys-root/genesys-signup-page/section/div/div[2]/div/div/form/input[1]')
# full_name_input.clear()
# full_name_input.send_keys(name)
# email_input =  driver.find_element_by_xpath('/html/body/genesys-root/genesys-signup-page/section/div/div[2]/div/div/form/input[2]')
# email_input.clear()
# email_input.send_keys(email)
# password_input = driver.find_element_by_xpath('/html/body/genesys-root/genesys-signup-page/section/div/div[2]/div/div/form/input[3]')
# password_input.clear()
# password_input.send_keys(password)
# password_input.send_keys(Keys.RETURN)