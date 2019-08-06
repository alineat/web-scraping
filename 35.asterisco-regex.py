import re

# caracter "*": possibilita que o caracter anterior pode ser correspondido zero ou mais vezes
# Sem *:
regex = re.compile('aaa')
print(regex.match('a'))  # retorna None, para dar match precisaria ter 3 as

# Com *:
regex = re.compile('a*')
print(regex.match('aaaa'))
print(regex.match(''))

# Pode usar a classe de caracteres
regex = re.compile('[a-d]*')  # a, b, c ou d podem vir quantas vezes quiser e em qualquer ordem
print(regex.match('bbb'))
print(regex.match('bbadccc'))
