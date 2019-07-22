# Faça uma lista aninhada com os valores:
# 0  1  2  3  4
# 5  6  7  8  9
# 10 11 12 13 14
# 15 16 17 18 19
# 20 21 22 23 24

# Sem list comprehension
lista = []

for linha in range(0, 25, 5):
    lista_interna = []
    for coluna in range(linha, linha+5):
        lista_interna.append(coluna)
    lista.append(lista_interna)
print('Lista sem list comprehension: ')

for linha in lista:
    print(linha)

# Com list comprehension
lista_c = [[coluna for coluna in range(linha, linha+5)] for linha in range(0, 25, 5)]
print('Lista com list comprehension: ')
for linha in lista_c:
    print(linha)
