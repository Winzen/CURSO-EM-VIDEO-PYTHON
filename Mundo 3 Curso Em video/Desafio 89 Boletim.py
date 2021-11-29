l = list()
ct = list()
while True:
    r = input("Nome do aluno:")
    ct.append(r)
    for x in range(1, 3):
        r = float(input(f"Nota {x}:"))
        ct.append(r)
    ct.append((ct[1] + ct[2]) / 2)
    l.append(ct[:])
    a = ' '
    while a not in "SsNn":
        a = input("Quer continuar?[S/N]:")
        if a in "Ss":
            ct.clear()
    if a in "Nn":
        break
print(f"{'=='*30}\n{'No.Nome':<10}{'Media':>10}\n{'--'*20}")
for x, z in enumerate(l):
    print(f"{x:<}  {z[0]:<10} {z[3]:>5.1f}")
while r != 999:
    a = int(input(f"{'-+'*20}\nDigite '999' para parar\nMostrar notas de qual aluno:"))
    print(f"Notas de {l[a][0]} são {l[a][1:3]}")
print("Obrigado!!!")

