salario = float(input("Digite o Valor do seu Salário: "))

if salario <= 1000:
    print(f"Valor do seu aumento é de 10%!")
    print(salario * 1.1)

else:
    print(f"Valor do seu aumento é de 5%!")
    print(salario * 1.05)

