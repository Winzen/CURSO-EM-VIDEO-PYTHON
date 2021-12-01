n = 0
while not n == 1:
    m = input("Responda com 'M' ou 'F'\nQual é seu sexo:").lower()
    if m in "Mm" or m in "Ff":
        n = n + 1
        print("Registrado")
    else:
        print("Tente novamente")
