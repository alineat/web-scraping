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

body = soup.body
p = soup.body.p

# body - contents

#print(body.contents)

# .next_sibling

print(p.next_sibling.next_sibling)  # uso ".next_sibling" duas vezes, pois tenho o caracter \n, se não eu não consigo
# me mover para a próxima tag
