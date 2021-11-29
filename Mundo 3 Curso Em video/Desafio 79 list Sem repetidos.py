l = list()
p = 0
while p == 0:
    s = ' '
    r = int(input("Digite um valor:"))
    if l.count(r) == 0:
        l.append(r)
        print("Valor Guardado com sucesso")
        while s not in "SsNn":
            s = input("Quer continuar?[S/N]:")
            if s in "Nn":
                print(f"{'-*-'*20}\nValores digitados:{sorted(l)}")
                p += 1
                break
    else:
        print("Tente outro numero..")

