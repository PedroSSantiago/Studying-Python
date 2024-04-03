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
lado_1 = float(input("Digite o valor do lado 1: "))
lado_2 = float(input("Digite o valor do lado 2: "))
lado_3 = float(input("Digite o valor do lado 3: "))
if lado_1 == lado_2 == lado_3:
    print("É um triângulo equilátero.")
elif lado_1 == lado_2 or lado_2 == lado_3 or lado_1 == lado_3:
    print("É um triângulo isóceles.")
else:
    print("É um triângulo escaleno.")
