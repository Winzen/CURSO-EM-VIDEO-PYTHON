x = int(input("Digite o numero que sera fatoriado:"))
f = x
g = x
for c in range(x-1, 1, -1):
    g = c * g
print(f"O faotiral do numero {f} é: {g}")