from bs4 import BeautifulSoup


def leia_arquivo():
    '''
    -> Lê um arquivo HTML.
    :return: os dados do arquivo HTML.
    '''
    arquivo = open('20.intro-to-soup-html.html')
    dado = arquivo.read()
    arquivo.close()
    return dado


soup = BeautifulSoup(leia_arquivo(), 'lxml')
title = soup.title
print(title)

parent = title.parent
print(parent)
print(parent.name)

# Quem é o pai do html?
html = soup.html
print(type(html.parent))

# Quem é o pai do soup
print(soup.parent)
