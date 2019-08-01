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

# .contents: retorna os filhos diretos da tag
'''
body = soup.body
print(body.contents)
print(len(body.contents))
'''

'''
body = soup.body
children = [child for child in body.contents if child != '\n']
print(children)
print(len(children))
'''

# .descendants: retorna todos os filhos da tag e o gerador
for indice, child in enumerate(soup.head.descendants):
    print(indice)
    print(child if child != '\n' else '\\n')
