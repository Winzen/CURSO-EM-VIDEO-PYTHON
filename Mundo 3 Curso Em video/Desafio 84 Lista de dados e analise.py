l = list()
t = list()
while True:
    t.append(input("Nome:"))
    t.append(float(input("Peso:")))
    l.append(t[:])
    t.clear()
    r = ' '
    while r not in "SsNn":
        r = input("Quer continuar?[S/N]:")
    if r in "Nn":
        break
for x, c in enumerate(l):
    if x == 0:
        max = min = c[1]
    if c[1] >= max:
        max = c[1]
    elif c[1] <= min:
        min = c[1]
print(f"{'--'*20}\nNumero de cadastro:{len(l)}")
print(f"Maior peso: {max}:", end=", ")
for x in l:
    if x[1] == max:
        print(x[0], end=" ")
print(f"\nMenor peso: {min}:", end=", ")
for x in l:
    if x[1] == min:
        print(x[0], end=" ")



