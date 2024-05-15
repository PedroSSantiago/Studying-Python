numeros = []

for i in range(10):
    num = float(input(f'Digite o {i + 1} numeros: '))
    numeros.append(num)

print(numeros)
numeros.reverse()
print(numeros)