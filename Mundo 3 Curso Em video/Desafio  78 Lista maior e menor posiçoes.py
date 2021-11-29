mi = list()
m = list()
v = list()
for x in range(5):
    v.append(int(input(f"Digite um valor para a posição {x}:")))
for z, f in enumerate(v):
    if f >= max(v):
        m.append(z)
    if f <= min(v):
        mi.append(z)
print(f"\n{'-+'*30}\nOs valores digitados foram: {v}")
print(f"O menor valor digitado foi {min(v)} na posição:", end=" ")
for t in mi:
    print(t, end="..")
print(f"\nO maior valor digitado foi o {max(v)} na posição:", end="")
for c in m:
    print(c, end="...")

