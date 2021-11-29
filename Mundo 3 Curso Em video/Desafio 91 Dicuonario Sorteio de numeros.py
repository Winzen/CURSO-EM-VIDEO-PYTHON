from random import randint
from time import sleep
d = dict()
l = list()
sl = list()
print("Valores Sorteados:")
for x in range(1, 5):
    d[f'jogador'] = f"Jogador {x}"
    d[f'numero'] = randint(1, 6)
    sl.append(d[f'numero'])
    print(f"O {d['jogador']} tirou {d['numero']}")
    sleep(0.75)
    l.append(d.copy())
sl.sort(reverse=True)
sleep(0.75)
print("\nValores Sorteados:")
for b, h in enumerate(sl):
    for x in l:
        if x['numero'] == h:
            print(f"{b+1}° Lugar: {x['jogador']} com {x['numero']}")
            l.remove(x)
            sleep(0.75)
            break

