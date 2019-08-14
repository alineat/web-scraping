from bs4 import BeautifulSoup


def read_file():
    file = open('43.consumer_reports.txt')
    data = file.read()
    file.close()
    return data


soup = BeautifulSoup(read_file(), 'lxml')

# Usando list comprehensions
'''
products = {}
product_names = [a.string for a in soup.find_all('a', class_='products-a-z__results__item')]
product_links = [a['href'] for a in soup.find_all('a', class_='products-a-z__results__item')]
'''

'''
OU
items = soup.find_all('a', attrs={'class': 'products-a-z__results__item'})
products = {item.string: item.get('href') for item in items}

for key, value in products.items():
    print(key, ':', ' http://www.consumerreports.org', value)
'''

# Ou, usar dictionary comprehension. Fica mais legível, economiza memória e tempo.
products = {a.string.strip(): a['href'] for a in soup.find_all('a', class_='products-a-z__results__item')}
#products = {a.string: a['href'] for a in soup.find_all('a', class_='products-a-z__results__item')}

for key, value in products.items():
    print(f'{key}: https://www.consumerreports.org{value}')
print(products)
