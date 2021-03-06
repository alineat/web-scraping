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

# Navigable strings - para acessar o conteúdo das tags, use o método <.string>
title = soup.title
print(title.string)
print(title)

# Para substituir o conteúdo da string, use <.replace_with("")>
print(f'Título antes: {title}')
title.string.replace_with("title has been changed")
print(f'Título depois: {title}')
