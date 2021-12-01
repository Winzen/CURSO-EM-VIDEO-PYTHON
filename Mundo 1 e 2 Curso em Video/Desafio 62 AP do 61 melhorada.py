a = 10
f = 0
tp = 0
p = 0
x = 0
ct = 0
ctm = 0
while f == 0:
    g = x
    if p == 0:
        x = int(input("\nPrimeiro termo da PA:")), int(input("Razão da PA:"))
        tp = x[0]
        p = p + 1
        print("\nOs 10 primeiros termos da sua PA são:")
    elif p != 0:
        ctm = ctm + 1
        ct = ct + 1
        print("", end=" ")
        print(ct * x[1], end=' ')
        if ctm == a:
            h = int(input("\nQuer fazer mais termos?\n 1 - Sim\n 2 - Não\nSua opção:"))
            if h == 2:
                print(f"\nForam feitos {ct} termos, nessa sessão")
                o = int(input("\nQuer uma nova pa?\n 1 - Sim\n 2 - Não\nSua opção:"))
                if o == 1:
                    p = p - 1
                    ct = 0
                    ctm = 0
                else:
                    print("\nFechando programa...")
                    f = f + 1

            else:
                a = int(input("Quantos mais termos:"))
                ctm = 0