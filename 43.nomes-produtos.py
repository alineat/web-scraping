from bs4 import BeautifulSoup
import re


def read_file():
    file = open('43.consumer_reports.txt')
    data = file.read()
    file.close()
    return data


soup = BeautifulSoup(read_file(), 'lxml')
all_divs = soup.find_all('a', attrs={'class': 'products-a-z__results__item'})
'''
for div in all_divs:
    print(div)
'''

products = [a.string for a in all_divs]
for product in products:
    print(product)
