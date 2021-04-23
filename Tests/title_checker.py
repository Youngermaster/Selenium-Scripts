import pytest
from selenium import webdriver
driver = webdriver.Chrome()


def test_answer():
    driver.get('https://www.google.com')
    print(driver.title)
    assert driver.title == 'Google'
    driver.close()
