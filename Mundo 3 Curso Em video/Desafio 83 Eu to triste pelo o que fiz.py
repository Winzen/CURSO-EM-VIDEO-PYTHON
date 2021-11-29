e = input("Digite sua expressão:")
p = list()
for x in e:
    if x in "(":
        p.append(x)
    elif x in ")":
        if len(p) > 0:
            p.remove("(")
        else:
            p.append(")")
print("Expressão valida" if len(p) == 0 else "Expressão não valida")

