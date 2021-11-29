t = list()
g = list()
c = b = p = 0
while c != 3:
    g.append(int(input(f"Digite um valor[{c},{b}]:")))
    b += 1
    if b == 3:
        t.append(g[:]), g.clear()
        c += 1
        b = 0
print('--'*20)
for j in t[0]:
    if j % 2 == 0:
        p += j
    print(f"[{j:^5}]", end="")
print()
for j in t[1]:
    if j % 2 == 0:
        p += j
    print(f"[{j:^5}]", end='')
print()
for j in t[2]:
    if j % 2 == 0:
        p += j
    print(f"[{j:^5}]", end='')
print(f"\n{'--'*20}\nA soma dos numeros Paress digitados: {p}")
print(f"O maior valor da segunda linha é {max(t[1])}")
print(f"A soma da terceira coluna: {t[0][2]+t[1][2]+t[2][2]}")