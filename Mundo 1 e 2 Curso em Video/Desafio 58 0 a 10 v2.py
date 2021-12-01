import random
from time import sleep
f = 0
tot = 0
while not f == 1:
    x = int(input(f"{'--'*20}\n\nDigite sua escolha:"))
    r = random.randint(0, 10)
    tot = tot + 1
    if x != r:
        print(f"{'--'*20}\n\33[1:31mTente novamente!!")
        print(f"\33[1:31mComputador escolheu {r} x {x} Foi sua escolha\33[m")
    else:
        print(f"\33[1:33mComputador escolheu {r} x {x} Foi sua escolha")
        print("\n\n\33[1:33mVocê acertou!!")
        print(f"Você tento um total de {tot}° vez.")
        f = f + 1

