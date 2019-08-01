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


# Faça a sopa. Síntaxe -> BeautifulSoup(html_data, parser).
arquivo_html = leia_arquivo()
soup = BeautifulSoup(arquivo_html, 'lxml')  # se não tiver inatalado lxml, use 'html.parser'
print(soup.prettify())
