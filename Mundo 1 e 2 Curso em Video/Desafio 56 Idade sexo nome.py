import time
mn = 0
p1 = 0, 0, 0
hm = 0
nhm = 0
mid = 0
g = 0
ihm = 0
print("Analise de grupo\n\nObs:Escreva a categoria 'sexo' com 'Feminino' ou 'Masculino', 'F' ou 'M'.")
time.sleep(2)
for x in range(1, 5):
    print("--"*20)
    print(f"{x}° Pessoa")
    p1 = input("Nome:"), int(input("Idade:")), input("Sexo:")
    g = p1[2].lower()
    if g == "f" and p1[1] < 20:
        for j in range(1, 2):
            mn += j
    elif g == "m" and p1[1] >= hm:
            hm = p1[1]
            nhm = p1[0]
            ihm = p1[1]
    mid += p1[1]
mid = mid/4
print(f"A media de idade do grupo é {mid:.1f} anos")
print(f"Homem com a maior idade tem {ihm} e é o {nhm}")
print(f"O numero de mulheres com menos de 20 anos é: {mn}")



