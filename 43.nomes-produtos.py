from bs4 import BeautifulSoup
import re


def read_file():
    file = open('43.consumer_reports.txt')
    data = file.read()
    file.close()
    return data


soup = BeautifulSoup(read_file(), 'lxml')
all_divs = soup.find_all('div', attrs={'class': 'crux-body-copy'})

products = [div.a.string for div in all_divs]
for product in products:
    print(product)
