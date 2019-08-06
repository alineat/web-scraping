from bs4 import BeautifulSoup
import re


def leia_arquivo():
    '''
    -> Lê um arquivo HTML.
    :return: os dados do arquivo HTML.
    '''
    arquivo = open('27.intro-to-soup-html.html')
    dado = arquivo.read()
    arquivo.close()
    return dado


soup = BeautifulSoup(leia_arquivo(), 'lxml')

# Métodos de pesquisa: find() e find_all(), em geral recebe o nome da tag como parâmetro
# Tipos de filtros usados para extrair tags: string, regular expression e lista .
# Filtros usados como parâmetros nos métodos find e find_all

# String, encontra todas as tags passadas como parâmetro
print(soup.find_all('b'))

# Regular Expression
regex = re.compile('^b')  # retorna qualquer string que comece com o caracter "b"
for tag in soup.find_all(regex):
    print(tag.name)

regex = re.compile('t')  # tags que contenham "t"
for tag in soup.find_all(regex):
    print(tag.name)

# Lista
for tag in soup.find_all(['a','b']):  # todas as tags a e b
    print(tag.name)


# Funções - find_all aceita funções como parâmetro


def has_class(tag):
    return tag.has_attr('class')


for tag in soup.find_all(has_class):
    print(tag.name)
