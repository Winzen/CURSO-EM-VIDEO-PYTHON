n = int(input("Gostaria de ver quais numero são primos até qual intervalo:"))
for x in range(1, n+1):
    if x == 3 or x == 2 or x == 7 or x == 5:
        print(f"{x} é um Numero primo")
    if x > 1 and x % 2 != 0 and x % x == 0 and x % 1 == 0 and x % 5 != 0 and x % 7 != 0 and x % 6 != 0 and x % 4 != 0 and x % 3 != 0:
        print(f"{x} é um Numero primo")
#else:
    #print("Não é um numero primo")