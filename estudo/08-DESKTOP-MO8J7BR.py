"""
20) Desenvolva um script em linguagem Python que peça os 3 lados de um triângulo. O
programa deverá informar se os valores podem formar um triângulo. Indique, caso os
lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o
terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes.
"""
base = float(input("Digite o valor da base: "))
lado_1 = float(input("Digite o valor do lado 1: "))
lado_2 = float(input("Digite o valor do lado 2: "))
if base <= lado_1 + lado_2:
    if base == lado_1 == lado_2:
        print("É um triângulo equilátero.")
    elif base == lado_1 or lado_2 == lado_1 or base == lado_2:
        print("É um triângulo isóceles.")
    else:
        print("É um triângulo escaleno.")
else:
    print("Esse triangulo não pode ser formado")
