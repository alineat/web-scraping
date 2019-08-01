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
p = soup.body.p

# .next_siblings

for sibling in p.next_siblings:
    #print(sibling.name if sibling != '\n' else '')
    pass

# .previous_siblings

for sibling in p.previous_siblings:
    print(sibling if sibling  != '\n' else '')
