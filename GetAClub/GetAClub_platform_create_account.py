from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Imports a random password generator
#from generate_password import generate_password_with_special_characters

# Use pip install names
#import names

def click_element_by_xpath(xpath):
    element_to_click = WebDriverWait(driver, 30).until(lambda x: x.find_element_by_xpath(xpath))
    element_to_click.click()

if __name__ == "__main__":
    PATH = 'C:\Program Files (x86)\chromedriver.exe'
    driver = webdriver.Chrome(PATH)

    driver.get('https://geta-client-webapp-dev.azurewebsites.net/#/landing')

    # SignUp button
    click_element_by_xpath('/html/body/genesys-root/genesys-landing-page/section/div/div/div/swiper/div/div[1]/div[2]/div/div[3]/button[1]')

    # element_to_click = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath('/html/body/genesys-root/genesys-signup-page/section/div/div[2]/div/form/div/div[1]/input'))
    # element_to_click.clear()
    # element_to_click.send_keys("March 19, 2001")
    #element_to_click.send_keys(Keys.RETURN)
    # Date selector
    click_element_by_xpath('/html/body/genesys-root/genesys-signup-page/section/div/div[2]/div/form/div/div[1]/input')
    # Year selection
    click_element_by_xpath('/html/body/div[3]/div[2]/div/mat-dialog-container/mat-datepicker-content/mat-calendar/mat-calendar-header/div/div/button[1]/span')
    # Backwards arrow button
    click_element_by_xpath('/html/body/div[3]/div[2]/div/mat-dialog-container/mat-datepicker-content/mat-calendar/mat-calendar-header/div/div/button[2]')
    # Selects the year, in this case 2001
    click_element_by_xpath('/html/body/div[3]/div[2]/div/mat-dialog-container/mat-datepicker-content/mat-calendar/div/mat-multi-year-view/table/tbody/tr[3]/td[2]/div[1]')
    # Selects the month, in this case march
    click_element_by_xpath('/html/body/div[3]/div[2]/div/mat-dialog-container/mat-datepicker-content/mat-calendar/div/mat-year-view/table/tbody/tr[2]/td[3]/div[1]')
    # Selects the day, in this case 19
    click_element_by_xpath('/html/body/div[3]/div[2]/div/mat-dialog-container/mat-datepicker-content/mat-calendar/div/mat-month-view/table/tbody/tr[4]/td[2]/div[1]')
    # Clicks submit
    click_element_by_xpath('/html/body/genesys-root/genesys-signup-page/section/div/div[2]/div/form/div/div[2]/button')
    # Click Avatar
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[src='/styles/assets/img/avatars/Avatar_Assasin.png'][type='image']"))).click()
    #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/genesys-root/genesys-signup-page/section/div/div[2]/div/genesys-gallery-form/section/div/div[2]/div[1]/div/img]"))).click()
    #click_element_by_xpath('') 

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