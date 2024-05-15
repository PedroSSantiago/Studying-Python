num = int(input("Digite um número inteiro: "))
div = 0
i = 1
print(f"divisores de {num}")
while i <= num:
    if num % i == 0: 
        div += 1
        print(i)
    i += 1
print(f"{num} tem {div} divisores.")
if div <= 2:
    print(f"{num} é primo!")
else:
    print(f"{num} não é primo!")


    
       
