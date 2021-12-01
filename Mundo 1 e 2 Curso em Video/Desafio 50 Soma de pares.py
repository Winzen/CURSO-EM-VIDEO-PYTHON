n = 0
for x in range(1, 7):
    t = int(input("Digite um numero:"))
    if t % 2 == 0:
        n += t
print(f"Soma de todos numeros pares: {n}")