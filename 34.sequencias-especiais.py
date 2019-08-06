import re

# Sequências Especiais -  podem ser usadas como equivalentes a character classes

# \d: correspondente de qualquer digito decimal. Equivale a classe de caracteres:[0-9]
regex = re.compile('\d')
print(regex.match('4'))

# \D: correspondente de qualquer caracter não-dígito. Equivale a classe de caracteres: [^0-9]
regex = re.compile('\D')
print(regex.match('a'))

# \s: correspondente de qualquer caracter de espaço em branco
regex = re.compile('\s')
print(regex.match(' '))

# \S: correspondente de qualquer caracter que não seja espaço em branco
regex = re.compile('\S')
print(regex.match('A'))

# \w: correspondente de qualquer caracter alfanumérico. Equivale a classe de caracteres: [a-zA-Z0-9]
regex = re.compile('\w')
print(regex.match('8'))

# \W: corresponde a qualquer caracter que não seja alfanumérico. Equivale a classe de caracteres: [^ a-zA-Z0-9]
regex = re.compile('\W')
print(regex.match(' '))
