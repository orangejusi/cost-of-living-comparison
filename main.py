from bs4 import BeautifulSoup
import requests
from datetime import datetime

# choose cities you want to webscrabe
city_1 = 'Hamburg'
city_2 = 'Berlin'
country = 'Germany'
country2 = 'Germany'

# Webscrape page for data (table)
url = f'https://www.numbeo.com/cost-of-living/compare_cities.jsp?country1={country}&country2={country2}&city1={city_1}&city2={city_2}&tracking=getDispatchComparison'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find('table', attrs={'class': 'data_wide_table new_bar_table cost_comparison_table'})
rows = table.find_all('tr')

# search for Cola data
cola_data = rows[7].text.split()
price_1 = cola_data[4]
price_2 = cola_data[6]

# print price for city
print(f'{city_1}: {price_1}€ \n{city_2}: {price_2}€')


date = datetime.today().strftime('%Y-%m-%d')

# list prices in file, orderd by date
document1 = open('Hamburg.txt', 'a')
document1.write(f'\n{date}/{price_1}')

document2 = open('Berlin.txt', 'a')
document2.write(f'\n{date}/{price_2}')

