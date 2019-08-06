import re

# caracter "?": o caracter anterior pode vir uma ou nenhuma vez.
regex = re.compile('a?b')
print(regex.match('b'))
print(regex.match('ab'))
print(regex.match('aab'))

# {m,n}: pode implementar qualquer um dos repetidores que vimos anteirormente. m e n são parâmetros integer.
# m: caracter anterior terá pelo menos m repetições; n: caracter anterior terá no máximo n repetições.
regex = re.compile('a{3,5}')  # aaa, aaaa ou aaaaa
print(regex.match('a'))  # None, já que espera pelo menos 3 repetições do a
print(regex.match('aaa'))
print(regex.match('aaaaaa'))  # retorna o match dos primeiros 5 "as" e não dos 6.

# {0,} substitui *
regex = re.compile('a{0,}')
print(regex.match('a'))
print(regex.match(''))

# {1,} substitui +
regex = re.compile('a{1,}')
print(regex.match(''))
print(regex.match('aaa'))

# {0,1} substitui ?
regex = re.compile('a{0,1}')
print(regex.match('a'))
print(regex.match('aa'))
