"""'

Faça um programa que leia 5 números e informe a soma e a média dos números.

"""
soma = 0
for i in range (5):
    n = int(input("Digite um Número: "))
    soma += n
media = soma / 5
print("Essa é sua média:", media)
print("Essa é sua soma:", soma)

