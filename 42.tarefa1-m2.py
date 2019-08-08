import re
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
header = {'user-agent': ua.chrome}
url = 'https://boston.craigslist.org/search/sof'
page = requests.get(url=url, headers=header, timeout=3)
soup = BeautifulSoup(page.content, 'lxml')

regex = re.compile(r'a')

for tag in soup(regex,class_="result-title hdrlnk"):
    print('Job: '+tag.text)
    print('URL: '+tag.get('href'))
    print('\n')
