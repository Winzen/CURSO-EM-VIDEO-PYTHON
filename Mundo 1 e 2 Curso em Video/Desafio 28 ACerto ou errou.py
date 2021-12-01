import random
x = int(input("Digite um numero de 0 a 5. E veja se consegue acerta qual numero a maquina escolheu.\n Digite seu numero aqui:"))
r = random.randrange(0,5)
if x==r:
    print(f"Nice! Você é um vidente. A maquina escolheu {r}\n Quem sabe o desenvolvedor coloque uma surpresinha para você.")
else:
    print("Não foi dessa vez. Mas tente mais uma vez")

