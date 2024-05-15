num = 0
soma = 0
n = 0
maior = -1
menor = 99999
while num != -1:
    num = int(input("digite um numero positivo (-1 para sair): "))
    if num >= 0:
        soma = soma + num
        n = n + 1
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print(f"Você digitou {n} numeros validos")
print(f"Soma: {soma}")
if n >0:
    print(f"media {soma/n:,.2f}")
print(f"Maior numero: {maior}")
print(f"Menor numero: {menor}")