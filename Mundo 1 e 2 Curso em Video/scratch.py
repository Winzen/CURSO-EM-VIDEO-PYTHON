num = (int(input('Primeiro Numero?')),
        int(input('sd Numero?')),
        int(input('ter Numero?')),
        int(input('Quar Numero?')))
print(f"Seus numeros são {num}")
print(f"O nove aparece {num.count(9)}")
if 3 in num:
    print(f"O valor 3 aparece na {num.index(3)+1}ª Posição ")
else:
    print("Não tem 3 aqui")
print("Os valores pares são os",end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')