import re

# caracter "+": possibilita que o caracter anterior possa ser correspondido uma ou mais vezes.
# Diferença - "*": 0 - infinito; "+": 1 - infinito

regex = re.compile('a+')
print(regex.match('aaaa'))
print(regex.match(''))

# Pode usar com classe de caracteres
regex = re.compile('[a-d]+')
print(regex.match('dddbaaaba'))
print(regex.match(''))
