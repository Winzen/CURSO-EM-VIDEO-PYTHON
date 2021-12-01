y = input("Qual ano quer saber se é bissexto?")
x = y.zfill(4)
g = len(x)-1
if int(x[g]) == 0:
    zb = int(x) % 400
    if zb == 0:
        print(f"O ano de {y} é Bissexto")
    else:
        print(f"O ano de {y} não vai ser Bissexto")
else:
    qb = int(x) % 4
    if qb == 0:
        print(f"O ano de {y} é BISSEXTO")
    else:
        print(f"O ano de {y} não é BISSEXTO")
