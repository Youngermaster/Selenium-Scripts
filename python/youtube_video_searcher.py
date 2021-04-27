from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://www.youtube.com")
elem = driver.find_element_by_name("search_query")
elem.clear()
elem.send_keys("Juan Manuel Young Hoyos")
elem.send_keys(Keys.RETURN)