from bs4 import BeautifulSoup


def read_file():
    file = open('22.tags.html')
    data = file.read()
    file.close()
    return data


soup = BeautifulSoup(read_file(), 'lxml')
meta = soup.meta

# modificando atributos
body = soup.body
body['style'] = 'some style'

# Multi valued attributes
print(body['class'])
