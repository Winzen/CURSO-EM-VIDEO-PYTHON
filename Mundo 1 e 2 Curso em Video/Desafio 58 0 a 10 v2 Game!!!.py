from random import randint
print("Vamos brincar um pouco.\nEu maquina, pensei em um numero de um 0 a 10.\nVocê poderia acertar?")
f = 0
cc = randint(0, 10)
ty = 0
while f == 0:
    x = int(input("\nEu pensei no numero:"))
    if x == cc:
        print(f"\n\33[1:32mAcertou!!!\33[m\nVocê precisou de {ty} tentativas.")
        f = f + 1
    else:
        ty = ty + 1
        print("\nTente novamente")
        if x <= cc:
            print("O numero é maior em.. :p")
        elif x >= cc:
            print("O numero é menor em... :p")
