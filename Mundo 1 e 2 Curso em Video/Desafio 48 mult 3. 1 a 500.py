c = 0
q = 0
for x in range(1, 501, 2):
    if x % 3 == 0:
        c += x
        for j in range(1, 2):
            q += j
print(f"Resultado dos numeros impares divisives por 3 até 500  é: {c}\nForam somados um total de {q}")