l1 = float(input("Primeiro lado do triangulo:"))
l2 = float(input("Segundo lado do triangulo:"))
l3 = float(input("Terceiro lado do triangulo:"))
la = l2 + l3, max(l3, l2) - min(l3, l2)
if la[0] > l1 > la[1]:
    print("Você pode fazer um triangulo com essas medidas")
    if l1 == l2 == l3:
        print("Tipo do triangulo: Equilátero\n Todos os seus lados são iguais")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("Tipo do triangulo: isósceles\n Pelo Menos dois lados iguais")
    else:
        print("Tipo do triangulo: Escanelo\nNenhum lado igual.")
else:
    print("Não é possivel fazer um triangulo com essas medidas.")
