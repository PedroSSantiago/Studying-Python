n1 = float(input("Digite o valor da sua compra: "))
n2 = float(input("Qual seu desconto? entre 0 e 1: "))
valor = n1 * n2 

if n2 > 1 or n2 < 0:
    print(f"O valor do desconto deve estar entre 0 e 1")
else:
    print(f"O valor do desconto é: {valor:.2f}")
print(f"O valor da compra é: {n1 - valor:.2f}")
