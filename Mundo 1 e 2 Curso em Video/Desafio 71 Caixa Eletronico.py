c = 1
cont = d = ci = di = de = u = 0
print("Banco do Soninho")
v = int(input("Valor do saque:R$"))
print("--"*30)
while c != 0:
    if cont == 0:
        d = 50
    elif cont == 1:
        d = 20
    elif cont == 2:
        d = 10
    elif cont == 3:
        d = 1
    g = v // d
    h = g * d
    c = v - h
    v = c
    if cont == 0:
        ci = g
    if cont == 1:
        di = g
    if cont == 2:
        de = g
    if cont == 3:
        u = g
    cont += 1
if ci > 0:
    print(f"Total de {ci} cedulas de R$50")
if di > 0:
    print(f"Total de {di} cedulas de R$20")
if de > 0:
    print(f"Total de {de} cedulas de R$10")
if u > 0:
    print(f"Total de {u} cedulas de R$1")
print(f"{'--'*20}\nVolte sempre ao Banco")




