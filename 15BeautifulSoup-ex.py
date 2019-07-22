from bs4 import BeautifulSoup
import requests

url = "http://example.com/"
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, 'html.parser')
tags = soup.find_all('a')

for tag in tags:
    print(tag.get('href'))
