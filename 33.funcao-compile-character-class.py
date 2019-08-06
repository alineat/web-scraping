import re  # módulo regular expression

# Expressão é compilada em bytecode e executada por um mecanismo de combinação escrito em C
# Usada para combinar caracteres, encontrar tags ou dados em uma árvore sintática
# Por ex. a expressão "abc" está na string "abcdef"
# Exceção: metacaracteres não dão "match"
# Lista de Metacaracteres: . ^ $ * + ? {} [] \ | ()

regex = re.compile('a')  # retorna um objeto regex
print(regex.match('a'))  # verifica se a expressão regex está na string.

regex = re.compile('ab')
print(regex.match('a'))  # Retorna None se não encontrar

# character class: aceita qualquer caracter que esteja dentro do []
regex = re.compile('[abc]')
print(regex.match('a'))
print(regex.match('d'))  # retorna None se  colocar qualquer coisa que não seja os caracteres dessa classe

regex = re.compile('[a-f]')  # posso escrever como intervalo
print(regex.match('e'))

regex = re.compile('[a-z]')
print(regex.match('C'))  # case sensitive

regex = re.compile('[a-zA-Z]')
print(regex.match('C'))

# Complementar do conjunto a-zA-Z, ou seja, todos os caracteres que não estejam nessa classe de caracteres
regex = re.compile('[^a-zA-Z]')
print(regex.match('1'))

# Metacaracteres perdem o seu significado quando estão dentro de uma classe de caracteres
regex = re.compile('[+]')
print(regex.match('+'))
