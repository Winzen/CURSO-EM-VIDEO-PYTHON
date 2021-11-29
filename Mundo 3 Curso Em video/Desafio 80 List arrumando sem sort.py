l = list()
for x in range(5):
    t = int(input("Digite um valor:"))
    if x == 0 or t >= max(l):
        print(f"O valor {t} vai ser colocado na ultima posição")
        l.append(t)
    elif t <= min(l):
        print(f"O valor {t} vai ser colocado na primeira posição")
        l.insert(0, t)
    elif min(l) < t < max(l):
        l.insert(1, t)
        print(f"O valor de {t} sera colocado na posição 1")
print(f"Sua lista é: {l}")