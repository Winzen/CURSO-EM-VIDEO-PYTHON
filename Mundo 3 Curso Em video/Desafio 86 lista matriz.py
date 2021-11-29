t = list()
g = list()
c = b = 0
while c != 3:
    g.append(int(input(f"Digite um valor[{c},{b}]:")))
    b += 1
    if b == 3:
        t.append(g[:]), g.clear()
        c += 1
        b = 0
print('--'*20)
print(t)
for j in t[0]:
    print(f"[  {j}  ]", end="")
print()
for j in t[1]:
    print(f"[  {j}  ]", end='')
print()
for j in t[2]:
    print(f"[  {j}  ]", end='')