# Encontre todos os números de 1-1000 que sejam divisíveis por 7
div7 = [num for num in range(1, 1001) if num % 7 == 0]
print(f'Divisíveis por 7: {div7}\n')

# Encontre todos os nºs de 1-1000 que contenham o nº 3
lista_do_tres = [num for num in range(1, 1001) if '3' in str(num)]
print(f'Nºs que contém o 3: {lista_do_tres}\n')

# Conte o número de espaços de uma string (normalmente usa-se teste.count(''))
teste = 'Encontre todos os espaços dessa string.'
espaco = [caracter for caracter in teste if caracter == ' ']
print(f'Nº de strings da frase: {len(espaco)}\n')

# Remova todas as vogais de uma string e faça uma lista de consoantes
string = 'Remova todas as vogais dessa string'
vogais = ['a', 'e', 'i', 'o', 'u', ' ']
consoantes = [letra for letra in string if letra.lower() not in vogais]
print(f'Consoantes: {consoantes}\n')

# Encontre todas as palavras da string que tenham menos de 4 letras
frase = 'Encontre todas as palavras que tenham menos de 4 letras nessa frase'
palavra4 = [palavra for palavra in frase.split() if len(palavra) < 4]
print(f'Palavras com menos de 4 letras: {palavra4}\n')

# Conte o comprimento de cada palavra em uma sentença
sentenca = 'Conte o comprimento de cada palavra desta sentença'
contagem = {palavra:len(palavra) for palavra in sentenca.split()}
print(f'Contagem: {contagem}\n')

# Encontre todos os números de 1-1000 que sejam divisíveis por números de um dígito (2-9), exceto o 1
divisiveis = [numero for numero in range(1, 1001) if True in [True for divisor in range(2, 10) if numero % divisor == 0]]
print(f'Divisíveis por números de um dígito: {divisiveis}\n')

# Para todos os números de 1-1000, ache o maior dígito único pelo qual os números sejam divisíveis
#       [divisor for divisor in range(1,1001) if number % divisor == 0]
resultado = {numero: max([divisor for divisor in range(1, 10) if numero % divisor == 0]) for numero in range(1, 1001)}
print(f'Maior divisor de um dígito: {resultado}')
