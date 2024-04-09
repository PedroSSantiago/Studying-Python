"""
18) Elabore um script em linguagem Python que leia três números e mostre o maior deles.
"""
# 19) Crie um script em linguagem Python que leia três números e mostre o maior e o menor deles.

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))
n3 = int(input("Digite um numero: "))
maior = max(n1,n2,n3)
menor = min(n1,n2,n3)
print("O maior número é:", maior)
print("O menor número é:", menor)
