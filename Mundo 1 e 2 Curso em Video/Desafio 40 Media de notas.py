print("Notas do aluno de 0 - 10")
x = float(input("Digite a primeira nota do aluno:"))
c = float(input("Segunda nota:"))
m = (x + c) / 2
print(f"Tirando {x} e {c} sua media vai ser {m:.1f}")
if m < 5:
    print("Você foi reprovado :c")
elif 5 <= m <= 6.9:
    print("Você ficou de recuperação")
elif m >= 7:
    print("Você foi aprovado")