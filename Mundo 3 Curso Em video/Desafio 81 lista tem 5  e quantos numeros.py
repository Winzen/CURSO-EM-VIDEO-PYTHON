l = list()
while True:
    r = int(input("Digite um valor:"))
    l.append(r)
    c = ' '
    while c not in "SsNn":
        c = input("Você quer continuar?[S/N]:")
        if c in "sS":
            print("Ok")
    if c in "Nn":
        break
l.sort(reverse=True)
print(f"O valor decrescente é : {l}")
print(f"Numeros digitados: {len(l)}")
print("O valor 5 faz parte da lista" if 5 in l else "O valor 5 não faz parte da lista")
