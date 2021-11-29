s = dict()
s['Nome'] = str(input("Nome do aluno:"))
s['Media'] = float(input(f"Media de {s['Nome']}: "))
if s['Media'] >= 7:
    s['Situação'] = "Aprovado"
elif 5 <= s['Media'] < 7:
    s['Situação'] = "Recuperação"
else:
    s['Situação'] = "Reprovado"
for x, f in s.items():
    print(f"{x} é igual a {f}")




