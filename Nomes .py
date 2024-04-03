n1 = "Pedro Schutzler Santiago"
n2 = "Lorenzo Viero Sartori"
n3 = "Matheus Justino"
palavra = input("Digite uma letra: ")

if palavra in n1:
    print (f"{palavra} existe em {n1} ")
else:
    print (f"{palavra} não existe em {n1} ")

if palavra in n2:
    print (f"{palavra} existe em {n2} ")
else:
    print (f"{palavra} não existe em {n2} ")
    
if palavra in n3:
    print (f"{palavra} existe em {n3} ")
else:
    print (f"{palavra} não existe em {n3} ")