cont = 1
p = n = 0
while True:
    if p == 0:
        n = int(input(f"{'--'*30}\nDigite um valor negativo para parar ' -1 '\nVocê quer a tabuada de que numero:"))
        print("")
        p += 1
        cont = 1
    if cont == 10:
        p -= 1

    if n >= 0:
        print(f"{n} x {cont} = {n * cont}")
        cont += 1
    else:
        print("Obrigado por usar o serviço de tabuada")
        break
