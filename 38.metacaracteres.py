import re

# "^": a string deve começar exatamente com a expressão informada
regex = re.compile('^abc')
print(regex.match('abc'))
print(regex.match('c'))

# "|": é o operador OR
regex = re.compile('a|b')
print(regex.match('a'))
print(regex.match('b'))
print(regex.match('ab'))

# "$": a string final deve corresponder exatamente a da expressão informada
regex = re.compile('abc$')
print(regex.match('c'))
print(regex.match('abc'))
print(regex.match('d'))

# Leia mais: https://www.thegeekstuff.com/2014/07/python-regex-examples/
