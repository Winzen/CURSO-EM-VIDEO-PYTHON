
x = int(input("Digite o numero que sera fatoriado:"))
t = x
f = 0
g = x
while f == 0:
    if x == 1:
        print(f"\nO fatorial do numero {t} é: {g}")
        print(end="")
        f = f + 1
    else:
        x = x - 1
        g = g * x
        print(x, end=">")