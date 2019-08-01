from bs4 import BeautifulSoup


def leia_arquivo():
    '''
    -> Lê um arquivo HTML.
    :return: os dados do arquivo HTML.
    '''
    arquivo = open('24.three-sisters.html')
    dado = arquivo.read()
    arquivo.close()
    return dado


soup = BeautifulSoup(leia_arquivo(), 'lxml')

# tag.contents: retorna a lista dos filhos
body = soup.body
for child in body.contents:
    #print(child if child is not None else '', end='\n\n\n\n')
    pass

# .children: retorna um iterador
for child in body.children:
    print(child if child is not None else '', end='\n\n\n\n')
