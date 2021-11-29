l = [[], []]
for x in range(7):
    f = int(input(f"{x+1}° - Digite um numero:"))
    l[0].append(f) if f % 2 == 0 else l[1].append(f)
print(f"Numeros pares:{sorted(l[0])}\nNumeros Impares:{sorted(l[1])}")