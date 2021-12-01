vc = float(input("Qual é o valor da casa?"))
s = float(input("Qual é o seu salario?"))
qa = int(input("enquantos anos pretende pagar?"))
anos = 12
par = vc / (qa*anos)
ex = s * 0.3
if par >= ex:
    print("Seu emprestimo foi negado!")
else:
    print(f"Seu emprestimo foi aprovado!\nSua prestação sera de {par:.2f}")


