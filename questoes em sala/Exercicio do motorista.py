vmax = float(input("Qual a velocidade permitida na via?: "))
vmo = float(input("Qual a velocidade do motorista?: "))

if vmo <= vmax:
    print("Voce esta dentro da velocidade permitida na via")
elif vmo <= vmax + 10:
    print("Esta acima da velocidade permitida na via")
    print(f"Você deve pagar uma multa de R$ R$ 85,13")
    pontos = 3
elif vmo <= vmax + 30:
    print("Esta ainda mais acima da velocidade permitida na via")
    print(f"Você deve pagar uma multa de R$127,69")
    pontos = 5
else:
    print("Esta bem fora da velocidade permitida na via")
    print(f"Você deve pagar uma multa de R$ 574,62")
    pontos = 7
match pontos:
    case 3:
        print("Multa Leve")
    case 5:
        print("Multa Media")
    case 7:
        print("Multa Gravíssima")






