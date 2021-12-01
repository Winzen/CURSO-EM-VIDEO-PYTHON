cont = soma = p = 0
while True:
    n = int(input(f"{'----'*20}\nDigite '999' para finalizar a contagem\nDigite um numero para a contagem? "))
    print('--'*20)
    if n == 999:
        print(f"Você digitou {cont} numeros\nA soma deles é {soma}")
        y = int(input("\nQuer fazer outra contagem?\n1 - Sim\n2 - Não\nDigite a opção: "))
        if y == 1:
            print("Voltando..")
            cont = soma = n = 0
        else:
            print("Obrigado por usar o serviço")
            break
    if n != 999 and n != 0:
        cont += 1
        soma += n
