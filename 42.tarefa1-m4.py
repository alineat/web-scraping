from bs4 import BeautifulSoup
import requests

url = "https://boston.craigslist.org/search/sof"
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, 'html.parser')
attr={'class':'result-title hdrlnk'}
tags = soup.find_all('a',attrs=attr)
#print(tags)
for tag in tags:
   print(tag.string)
   print(tag.get('href'))
