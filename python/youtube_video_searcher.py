from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get("https://www.youtube.com")
elem = driver.find_element_by_name("search_query")
elem.clear()
elem.send_keys("Juan Manuel Young Hoyos")
elem.send_keys(Keys.RETURN)