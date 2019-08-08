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

# parâmetros de find_all(name, attrs, recursive, string, limit, **kwargs)
# Parâmetro name: pode receber um objeto RegEx; string; True; ou função
a_tags = soup.find_all('a')
print(a_tags)  # retorna uma lista com todos os "as"
# ou
# for a in a_tags:
#     print(a)

# Parâmetro attrs: atributos de uma tag
attr = {'class': 'sister', 'id': 'link2'}
a2 = soup.find_all('a', attrs=attr)
print(a2)
# se eu quiser todas as tags de class "sister"
attr = {"class": "sister"}
tag_a = soup.find_all('a', attrs=attr)  # o "a" é desnecessário, já que todos os "as" tem classe "sister"
print(tag_a)

# Parâmetro limit: limita o número de buscas que será retornado
a_tags = soup.find_all('a',limit=2)
print(a_tags)

# Parâmetro String: a entrada é uma string ou um objeto RegEx. Retorna uma string navegável.
print('Procurando a string Elsie no meu documento:')
regex = re.compile('Elsie')
tag = soup.find_all(string=regex)
print(f'{tag}\n')

print('Busca da string \"story\":')
regex = re.compile('story')
tag = soup.find_all(string=regex)
print(f'{tag}\n')

# Parâmetro **kwargs (keyword arguments)
print('Busque as tags de class \"sister\":')
tags = soup.find_all(class_='sister')  # usar um ou + atributos da tag q quero encontrar: (find_all(id='link', href=...))
for tag in tags:
    print(tag)
print(f'Foram encontrados {len(tags)} tags com class \"sister\".\n')
# P.S: para escrever um atributo class use "class_", pois "class" é uma palavra-chave do Python

# Parâmetro recursive
# Ex: se eu quiser pesquisar nos filhos diretos do <html>, não preciso pesquisar no documento inteiro. "recursive" força
# o BS a olhar apenas nesse nível, do contrário e por padrão ele buscaria no documento inteiro a tag "title"
# (recursive=True é o padrão)
title = soup.find_all('title', recursive=False)  # só pesquisamos os descendentes diretos da tag
print(title)  # retorna uma lista vazia, pois só pode buscar nas tags body e head
