import datetime
dh = datetime.date.today().year
print("Digite anos de nascimentos para veremos quantos são de maiores e menores.")
dt = int(input("Data da primeira pessoa:")), int(input("Data da sd pessoa:")), int(input("Data da tr pessoa:")),int(input("Data da quarta pessoa:")), int(input("Data da quinta pessoa:")), int(input("Data da sexta pessoa:")), int(input("Data da Setima pessoa:"))
mn = 0
men = 0
for x in dt:
    x = dh - x
    if x >= 21:
        for m in range(1, 2):
            mn += m
    else:
        for n in range(1, 2):
            men += n
print(f"O numero de maiores de idade são {mn}")
print(f"Numero de menores de idade são {men}")





#for x in range(1, 8):
   # de = int(input(f"Idade da {x}° pessoa:")),
    #int(input(f"Idade da {x}° pessoa:"))

#for x in input(f"Digite a idade da ° pessoa: ") and range(8):

#print(x)