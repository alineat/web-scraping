from bs4 import BeautifulSoup


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
