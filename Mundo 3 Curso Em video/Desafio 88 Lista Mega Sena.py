import random
from time import sleep
t = list()
r = 0
h = int(input("Quantos jogos você quer que eu sortei:"))
for x in range(h):
    for n in range(6):
        while True:
            r = random.randint(1, 60)
            if t.count(r) == 0:
                t.append(r)
                break
    print(f"Jogo {x+1}°:{sorted(t)}")
    t.clear()
    sleep(0.65)