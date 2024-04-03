import math
raio = float(input("Digite o raio do Circulo: "))
n1 = int(input("Se quiser área digite 1, se quiser perímetro digite 2: "))
area = (math.pi * raio ** 2)
perimetro = (2 * math.pi * raio)
if n1 == 1:
    print(f"Valor da área é:{area:,.2f}")
if n1 == 2:
    print(f"Valor do perimetro é:{perimetro:,.2f}")
