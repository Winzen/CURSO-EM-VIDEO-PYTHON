l = list()
i = list()
p = list()
while True:
    n = int(input("Digite um valor:"))
    l.append(n)
    if n % 2 == 0:
        p.append(n)
    else:
        i.append(n)
    f = ' '
    while f not in "SsNn":
        f = input("Deseja continuar?[S/N]:")
    if f in "nN":
        break
print(f"Obrigado!!\nLista completa:{l}\nNumeros Pares da lista: {p}\nNumeros Impares a lista: {i}")