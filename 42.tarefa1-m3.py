import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# Create a header for our requests module
ua = UserAgent()
header = {"user-agent": ua.chrome}

# url to open
url = "https://boston.craigslist.org/search/sof"

# Open page
page = requests.get(url, headers=header)

# Parse html
soup = BeautifulSoup(page.content, "lxml")

attr = {"class": "result-title hdrlnk"}

for a in soup.find_all(name="a", attrs=attr):
    print("Job:", a.contents[0])
    print("URL:", a["href"])
