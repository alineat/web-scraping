from bs4 import BeautifulSoup
import requests

url = "http://example.com/"
resposta = requests.get(url)
dado = resposta.text
soup = BeautifulSoup(dado, 'html.parser')
tags = soup.find_all('a')

for tag in tags:
    print(tag.get('href'))
