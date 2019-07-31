from bs4 import BeautifulSoup


def read_file():
    file = open('24.three-sisters.html')
    data = file.read()
    file.close()
    return data


soup = BeautifulSoup(read_file(), 'lxml')
print(soup.prettify())


# example  -- direct

p = soup.p

print(p)



