from pyvirtualdisplay import Display
import pytest
from selenium import webdriver
driver = webdriver.Chrome()


def test_answer():
    display = Display(visible=0, size=(800, 800))  
    display.start()
    driver.get('https://www.google.com')
    print(driver.title)
    assert driver.title == 'Google'
    driver.close()
