n = ("Zero", "Um", "Dois", "Três", "Quadro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Catorze",\
"Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")
l = p = -1
while l == -1:
    while not 20 >= p >= 0:
        p = int(input("Digite um numero entre 0 e 20 para saber seu extenso:"))
        if not 20 >= p >= 0:
            print("Tente novamente")
    print(f"Você digitou o numero {n[p]}")
    r = " "
    while r not in "SsNn":
        r = input("Quer continuar?\n[S/N]:")
        if r in "Ss":
            p = -1
        else:
            print("Obrigado!!")
            l += 1


