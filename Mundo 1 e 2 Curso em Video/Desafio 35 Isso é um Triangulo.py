x = float(input("Qual é o tamanho da primeira linha para fazer o triangulo?"))
e = float(input("Segunda linha:"))
t = float(input("Terceira linha:"))
er = e + t
ty = max(e, t) - min(e, t)
if x < er and x > ty:
    print("Podemos fazer um triangulo com essas medidas")
else:
    print("Não podemos fazer um triangulo com essas medidas")
