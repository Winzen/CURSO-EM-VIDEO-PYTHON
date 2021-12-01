f = 0
p = 0
while f == 0:
    if p == 0:
        v = int(input("\nDigite dois valores que deseja trabalhar\nPrimeiro valor:")), int(input("Segundo Valor:"))
        p = p + 1
    print("\nO que você quer fazer com os valores?\n1 - Soma\n2 - Multiplicar \n3 - Maior \n4 - Novos Numeros\n5 - Sair do Programa")
    y = int(input("\nDigite sua opção:"))
    if y == 1:
        print(f"A soma dos valores {v[0]} + {v[1]} = {(v[0]) + (v[1])}")
        g = int(input("\n1 - voltar para o inicio\n2 - Sair do programa\nDigite sua opção:"))
        if g == 1:
            print("voltando para o inicio...")
        else:
            print("saindo....")
            f = f + 1
    elif y == 2:
        print(f"Seus valores multiplicados ficam: {v[0]} x {v[1]} = {v[0] * v[1]} ")
        g = int(input("\n1 - voltar para o inicio\n2 - Sair do programa\nDigite sua opção:"))
        if g == 1:
            print("voltando para o inicio...")
        else:
            print("saindo....")
            f = f + 1
    elif y == 3:
        print(f"O maior numero entre {v[0]} e {v[1]} é {max(v[0], v[1])}")
        g = int(input("\n1 - voltar para o menu\n2 - Sair do programa\nDigite sua opção:"))
        if g == 1:
            print("voltando para o menu...")
        else:
            print("saindo....")
            f = f + 1
    elif y == 4:
        print("Voltando para o inicio..")
        p = p - 1
    elif y == 5:
        print("Fechando programa..")
        f = f + 1
    else:
        print("Erro tente novamente")