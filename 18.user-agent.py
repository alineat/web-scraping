import requests
from fake_useragent import UserAgent

ua = UserAgent()
header = {'user-agent': ua.chrome}
print(ua.chrome)

pagina = requests.get('https://www.google.com', headers=header)
print(pagina.content)

# Timeout
page = requests.get('https://www.google.com', timeout=3)
