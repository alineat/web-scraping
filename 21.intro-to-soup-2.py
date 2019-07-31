import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
header = {'user-agent': ua.chrome}
google_site = requests.get('https://www.google.com', headers=header)

soup = BeautifulSoup(google_site.content, 'lxml')
print(soup.prettify())
