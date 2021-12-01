f = 0
tp = 0
p = 0
x = 0
ct = 0
while f == 0:
    g = x
    if p == 0:
        x = int(input("Primeiro termo da PA:")), int(input("Razão da PA:"))
        tp = x[0]
        p = p + 1
        print("\nOs 10 primeiros termos da sua PA são:")
    elif p != 0:
        ct = ct + 1
        print(ct * x[1], end='->')
        if ct == 10:
            h = int(input("\nQuer fazer uma nova PA?\n 1 - Sim\n 2 - Não\nSua opção:"))
            if h == 2:
                f = f + 1
            else:
                p = p - 1
                ct = 0