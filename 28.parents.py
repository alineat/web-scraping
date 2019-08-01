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

# .parents: retorna uma lista de pais
link = soup.a
print(f'link: {link}')
print(f'parents: {link.parents}')
print(f'parent: {link.parent}')
print(f'name: {link.parent.name}\n')

# Vamos iterar
for parent in link.parents:
    print(parent.name)
