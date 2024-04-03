import math
raio_maior = float(input("Digite valor raio maior: "))
raio_menor = float(input("Digite valor raio menor: "))
area_coroa = math.pi * (raio_maior**2 -(raio_menor**2))
print(f"Area da coroa circular é: {area_coroa:.2f}") 