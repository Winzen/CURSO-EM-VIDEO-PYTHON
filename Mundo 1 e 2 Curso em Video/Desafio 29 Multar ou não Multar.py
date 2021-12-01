x = float(input("Em que velocidade estava o carro:"))
if x > 80:
    n = (x-80)*7
    print(f"Velocidade muita alta! Velocidade maxima é de 80kh\nSugeita a multa de R$ {n}")
else:
    print("Velocidade dentro da permitida. Nenhuma multa será cobrada")