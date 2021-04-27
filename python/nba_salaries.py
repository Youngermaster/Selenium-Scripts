from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

driver = webdriver.Chrome()

driver.get('https://hoopshype.com/salaries/players/')

players = driver.find_elements_by_xpath('//td[@class="name"]')

players_list = []
for p in range(len(players)):
    players_list.append(players[p].text)

# Prints out all the players that we got
#print('Players:')
#print(players_list)

salaries = driver.find_elements_by_xpath('//td[@class="hh-salaries-sorted"]')
salaries_list = []
for s in range(len(salaries)):
    salaries_list.append(salaries[s].text)

# Prints out all the salaries that we got
#print('Salaries:')
#print(salaries_list)

# Prints how many players and salaries there are, and should be the same.
if len(players_list) > 1:
    print(f'There are {len(players_list)} players in the list.')
elif len(players_list) == 1:
    print('There is 1 player in the list.')
else:
    print('There are no players in the list.')

if len(salaries_list) > 1:
    print(f'There are {len(salaries_list)} players in the list.')
elif len(salaries_list) == 1:
    print('There is 1 player in the list.')
else:
    print('There are no players in the list.')
    

print(f'{players_list[1]} earns ${salaries_list[1]}')