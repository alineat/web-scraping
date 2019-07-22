# Revisão: list comprehension é uma forma mais limpa de criar e manusear listas
# Faça uma lista de valores aleatórios

import random

# Sem list comprehension
lista_numeros = []
for numero in range(0, 20):
    lista_numeros.append(random.randint(0, 100))
print(f'Lista aleatória sem list comprehension: {lista_numeros}')

# Com list comprehension
lista_c = [valor for valor in range(0,20+1)]     # síntaxe: valor + loop for
print(f'Lista de 0-20 com list comprehension: {lista_c}')

lista_c = [random.randint(0, 100) for valor in range(0, 20)]
print(f'Lista aleatória com list comprehension: {lista_c}')
