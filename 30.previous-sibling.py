from bs4 import BeautifulSoup


def leia_arquivo():
    '''
    -> Lê um arquivo HTML.
    :return: os dados do arquivo HTML.
    '''
    arquivo = open('27.three-sisters.html')
    dado = arquivo.read()
    arquivo.close()
    return dado


soup = BeautifulSoup(leia_arquivo(), 'lxml')
body = soup.body
print(soup.html.contents)

# do <body> vá para o irmão anterior <head>

print(body.previous_sibling.previous_sibling)
