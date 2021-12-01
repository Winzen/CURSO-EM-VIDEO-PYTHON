from random import randint
cont = 0
print("Vamos jogar PAR OU IMPAR!!!!!")
while True:
    x = int(input("Digite um valor para jogar:")), input("o numero final sera Impar ou Par?\nDIgite:[P/I]")
    cc = randint(0, 10)
    if x[1] in "Pp":
        rp = "Par"
    elif x[1] in "Ii":
        rp = "Impar"
    if (x[0] + cc) % 2 == 0:
        r = "Par"
    else:
        r = "Impar"
    print(f"Você jogou {x[0]} e o computador {cc}. Total de {x[0] + cc} deu {r} ")
    print("---"*20)
    if rp == r:
        print("Você ganhou!!!\nVamos jogar novamente..\nAté eu vencer. HAHAHAHAHAHHA")
        cont += 1
    else:
        print(f"Você perdeu :c\nMas eu ganhei. Então tudo bem! :D\nVocê ganhou {cont}° vezes.")
        break

