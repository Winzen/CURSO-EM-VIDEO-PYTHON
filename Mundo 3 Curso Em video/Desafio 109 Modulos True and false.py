from mundo.moeda import moeda

p = float(input("Digite o preço : R$"))
print(f"A metade de {moeda.fmoeda(p)} é {moeda.meio(p, True)}\nO dobro de {moeda.fmoeda(p)} é {moeda.dob(p, True)}\nO aumento de 10% de {moeda.fmoeda(p)} é {moeda.aumepot(p, 10, True)}\nReduzindo 13% de {moeda.fmoeda(p)} temos {moeda.dimpot(p, 13, True)}"
      f"")