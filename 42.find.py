from bs4 import BeautifulSoup
import re


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

# Parâmetros de find: find(name, attrs, recursive, string, **kwargs), exceto limit, já que find retorna apenas um objeto
# de cda vez. Caso haja múltiplos objetos, retorna o primeiro que encontrar.

tag = soup.find('a')
print(tag)
print(f'Foram encontrados: {len(tag)} tags <a>.')
