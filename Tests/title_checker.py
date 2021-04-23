from pyvirtualdisplay import Display
import pytest
from selenium import webdriver


def test_answer():
    display = Display(visible=0, size=(800, 800))  
    display.start()
    driver = webdriver.Chrome()
    driver.get('https://www.google.com')
    print(driver.title)
    assert driver.title == 'Google'
    driver.close()
