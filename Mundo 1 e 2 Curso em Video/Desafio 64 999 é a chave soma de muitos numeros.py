f = h = cont = soma = 0
while f == 0:
    if h == 999:
        print(f"\nVocê digito {cont} numeros.\nResultado da soma dos numeros digitados é: {soma}")
        l = int(input("Quer voltar a digitar somas?\n1 - Sim\n2 - Não\n Sua escolha aqui:"))
        if l == 1:
            cont = 0
            soma = 0
            h = 0
        else:
            print("Fechando programa..")
            f = f + 1
    else:
        h = int(input("\nDigite '999' para parar\n\nDigite um numero que sera somado:"))
        if h != 999:
            soma = soma + h
            cont = cont + 1