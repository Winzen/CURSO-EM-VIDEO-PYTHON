#chaves
f = 0
#Programa
soma = 0
ior = 0
nor = 0
cont = 0

while f == 0:
    x = int(input("Digite valor para media e maior/menor:"))
    cont = cont + 1
    if cont == 1:
        ior = nor = x
    else:
        if x > ior:
            ior = x
        if x < nor:
            nor = x
    soma = soma + x
    media = soma / cont
    y = int(input("\nQuer continuar a digitar valores?\n1 - Sim\n2 - Não\nSua escolha:"))
    if y == 2:
        print(f"\nA media dos valores ditados é: {media:.2f}\nO maior numero digitado é: {ior}\nO menor numero digitado é: {nor}")
        k = int(input("Quer uma nova conta?\n1 - Sim\n2 - Não\n Sua opção:"))
        if k == 1:
            soma = 0
            cont = 0
            ior = 0
            nor = 10000000 ** 1000000
        else:
            print("Fechando programa..")
            f = f + 1

