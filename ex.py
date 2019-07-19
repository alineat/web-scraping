numero3 = [num for num in range(1000) if '3' in str(num)]
print(numero3)

numero3 = []
for num in range(1000):
    if '3' in str(num):
        numero3.append(num)
print(numero3)