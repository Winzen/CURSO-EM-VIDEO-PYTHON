from random import randint
from time import sleep
def sort(a):
    print(f"Sorteando 5 valores da lista:", end=' ')
    for x in range(5):
        t = randint(1, 10)
        a.append(t)
        sleep(0.45)
        print(t, end=" ")
    print("PRONTO!", end=' ')
    print()
def sp(t):
    s = 0
    for x in t:
        if x % 2 == 0:
            s += x
    print(f"Somando os valores {t}, temos {s}")


a = list()
sort(a)
sp(a)



