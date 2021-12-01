x = int(input("Qual é o seu salario?"))
if x > 1250:
    au = x * 1.1
    print("Seu salario  vai ser aumentado para R${:.2f}".format(au))
else:
    bu = x * 1.15
    print("Seu selario sera aumentado para R${:.2f}".format(bu))