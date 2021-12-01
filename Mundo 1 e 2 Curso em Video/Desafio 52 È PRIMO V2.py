n = int(input("Digite um numero:"))
nd = 0
for x in range(1, n+1):
    d = n % x
    if d == 0:
        print(f"\33[1:33m{x}\33[m", end=' ')
        nd = nd + 1
    else:
        print(f"\33[1:31m{x}\33[m", end=" ")
if nd == 2:
    print(f"\nIsso é um numero primo!\nEle foi apenas dividido {nd} vezes.")
else:
    print(f"\nIsso não é um numero primo, pois foi divido {nd} vezes.")
