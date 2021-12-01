contt = y = x = h = f = conth = contm = 0
while f == 0:
    print(f"{'---'*30}\nCADASTRE DADOS\n{'--'*30}")
    while True:
        x = int(input("Idade:"))
        if x > 0:
            break
    while True:
        y = input("Sexo:[M/F]")
        if y in "FfMm":
            break
    if x > 18:
        contt += 1
    if y in "Mm":
        conth += 1
    if x < 20 and y in "Ff":
        contm += 1
    while True:
        h = input("Quer continuar?\nOpção[S/N]:")
        if h in "Ss":
            print("")
            break
        elif h in "Nn":
            print(f"Obrigado!\nUm Total de {contt} cadastros foram maior que 18 anos.\nAo todo temos {conth} homens cadastrados\nE temos {contm} mulheres com menos de 20 anos.")
            f += 1
            break
