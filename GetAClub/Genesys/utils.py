from selenium import webdriver
import names

PATH = 'C:\Program Files (x86)\chromedriver.exe'
DRIVER = webdriver.Chrome(PATH)

def create_club_name():
    return names.get_full_name()