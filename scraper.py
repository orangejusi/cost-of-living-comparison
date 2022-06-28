from bs4 import BeautifulSoup
import requests
import json
from datetime import datetime


date = datetime.today().strftime('%Y-%m-%d')

# choose cities to webscrape
city_1 = 'Hamburg'
city_2 = 'Berlin'
country = 'Germany'
country2 = 'Germany'

# Webscrape page data (table)
url = f'https://www.numbeo.com/cost-of-living/compare_cities.jsp?country1={country}&country2={country2}&city1={city_1}&city2={city_2}&tracking=getDispatchComparison'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find('table', attrs={'class': 'data_wide_table new_bar_table cost_comparison_table'})
rows = table.find_all('tr')

# create dictionary date in dictionary 'dictionary'
dictionary = {date: {}}

# filter for important information
for i, x in enumerate(rows[1:9]):
    no_text = x.text.split()
    dictionary[date][' '.join(no_text[0:-6])] = (float(no_text[-6]), float(no_text[-4]))

# open file and save data
with open('prices.json') as file:
    data = json.load(file)

with open('prices.json', 'w') as file:
    res = data | dictionary
    json.dump(res, file)
