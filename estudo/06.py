"""
15) João Pescador, homem de bem, comprou um microcomputador para controlar o
rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o
estabelecido pelo regulamento de pesca do Estado (50 quilos) deve pagar uma multa de
R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável
peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de
quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima
os dados do programa com as mensagens adequadas.
"""
peso_max = 50
valor_da_multa = 4
multa = 0
peso = 0
peso = float(input("Peso do peixe: "))
if peso>50:
    excesso = peso - 50
    multa = excesso * valor_da_multa
    print("Valor excedido do peso: ", excesso)
    print("Valor da multa: ", multa)
else:
    print("Não pagará multa.")



