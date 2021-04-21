from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import DRIVER as driver
# Imports a random password generator
from generate_password import get_simple_password

# Use pip install names
import names


def click_element_by_xpath(xpath):
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, xpath))).click()


def generate_user():
    name = f'{names.get_last_name()}{names.get_first_name()}'
    email = name + '@gmail.com'
    password = get_simple_password(10)

    return name, email, password


def store_user(name, email, password):
    file = open("emailsAndPasswords.txt", "a")
    file.write("________________\n")
    file.write(f"\nName: {name}")
    file.write(f"\nEmail: {email}")
    file.write(f"\nPassword: {password}\n")
    file.write("________________\n")
    file.close()


def create_account():
    driver.get('https://geta-client-webapp-dev.azurewebsites.net/#/landing')

    # SignUp button
    click_element_by_xpath(
        '//*[@id="swiper-wrapper-1a2e546097e3d932"]/div[2]/div/div[4]/button[1]')
    # Date selector
    click_element_by_xpath(
        '/html/body/genesys-root/genesys-signup-page/section/div/div[2]/div/form/div/div[1]/input')
    # Year selection
    click_element_by_xpath(
        '/html/body/div[3]/div[2]/div/mat-dialog-container/mat-datepicker-content/div[2]/mat-calendar/mat-calendar-header/div/div/button[1]')
   
    # Selects the year, in this case 2001
    click_element_by_xpath(
        '/html/body/div[3]/div[2]/div/mat-dialog-container/mat-datepicker-content/div[2]/mat-calendar/div/mat-multi-year-view/table/tbody/tr[6]/td[2]')
    # Selects the month, in this case march
    click_element_by_xpath(
        '/html/body/div[3]/div[2]/div/mat-dialog-container/mat-datepicker-content/div[2]/mat-calendar/div/mat-year-view/table/tbody/tr[2]/td[3]')
    # Selects the day, in this case 19
    click_element_by_xpath(
        '/html/body/div[3]/div[2]/div/mat-dialog-container/mat-datepicker-content/div[2]/mat-calendar/div/mat-month-view/table/tbody/tr[4]/td[2]')
    # Clicks submit
    click_element_by_xpath(
        '//html/body/genesys-root/genesys-signup-page/section/div/div[2]/div/form/div/div[2]/button')
    # Click Avatar
    click_element_by_xpath(
        '/html/body/genesys-root/genesys-signup-page/section/div/div[2]/div/genesys-gallery-form/section/div/div[2]/div[1]/div/img')

    name, email, password = generate_user()

    store_user(name, email, password)

    full_name_input = driver.find_element_by_xpath(
        '/html/body/genesys-root/genesys-signup-page/section/div/div[2]/div/div/form/input[1]')
    full_name_input.clear()
    full_name_input.send_keys(name)
    email_input = driver.find_element_by_xpath(
        '/html/body/genesys-root/genesys-signup-page/section/div/div[2]/div/div/form/input[2]')
    email_input.clear()
    email_input.send_keys(email)
    password_input = driver.find_element_by_xpath(
        '/html/body/genesys-root/genesys-signup-page/section/div/div[2]/div/div/form/input[3]')
    password_input.clear()
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)


def skip_tutorial():
    click_element_by_xpath(
        '/html/body/genesys-root/genesys-master-page/genesys-ctrl-tour/div/a')


if __name__ == "__main__":
    create_account()
    skip_tutorial()
