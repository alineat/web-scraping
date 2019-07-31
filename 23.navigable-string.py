from bs4 import BeautifulSoup


def read_file():
    file = open('20.intro-to-soup-html.html')
    data = file.read()
    file.close()
    return data


soup = BeautifulSoup(read_file(), 'lxml')

# Navigable strings - para acessar o conteúdo das tags, use o método <.string>
title = soup.title
print(title.string)
print(title)

# Para substituir o conteúdo da string, use <.replace_with("")>
print(f'Título antes: {title}')
title.string.replace_with("title has been changed")
print(f'Título depois: {title}')
