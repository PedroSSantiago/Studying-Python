"""
14) Criar um script em linguagem Python que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido
mês.

"""
salario = 0
horas = 0
salario = float(input("Digite o seu salario por hora: "))
horas = int(input("Quantas horas voce trabalha?: "))
soma = salario * horas
print("Esse é seu salario mensal:", soma)