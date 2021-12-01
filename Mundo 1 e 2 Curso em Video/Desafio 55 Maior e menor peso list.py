mn = 300
m = 0
for t in range(1, 6):
    x = float(input(f"Qual é seu peso da {t}ºPessoa:"))
    if x >= m:
        m = x
    elif x <= mn:
        mn = x
print(f"Maior peso registrado foi o {m}kg")
print(f"Menor peso registrado foi {mn}kg")