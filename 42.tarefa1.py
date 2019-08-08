from bs4 import BeautifulSoup
import requests

url = "https://boston.craigslist.org/search/sof"
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, 'lxml')
tags = soup.find_all("a", {"class": "result-title hdrlnk"})
print(tags)

for tag in tags:
    print('\nJob: ',end="")
    print(tag.string)
    print('URL: ', end="")
    print(tag.get('href'))
