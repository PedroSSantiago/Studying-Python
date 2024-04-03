""" 
Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

"""
n1 = int(input("Digite sua nota: "))
if n1 <0 or n1 >10:
    print("Nota Incorreta.")
else:
    print("Nota Válida.")
