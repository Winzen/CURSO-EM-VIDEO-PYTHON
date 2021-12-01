f1 = 0
f2 = 1
f3 = 0
f = 0
p = 0
cont = 0
#1 + 1 = 2
while f == 0:
    if p == 0:
        r = int(input("Quantos termos você quer da sequencia Fibonacci?\nDigite aqui:"))
        p = p + 1
    else:
        f3 = f2 + f1
        f1 = f2
        f2 = f3
        cont = cont + 1
        print(f3, end=' ')
        if cont == r:
            h = int(input("\nQuer colocar um novo numero de termos?\n1 - Sim\n2 - Não\nSua Opção:"))
            if h == 1:
                p = p - 1
                cont = 0
                f1 = 0
                f3 = 0
                f2 = 1
            else:
                print("\nFechando programa..")
                f = f + 1