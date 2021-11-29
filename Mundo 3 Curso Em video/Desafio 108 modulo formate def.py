from mundo.moeda import moeda

p = float(input("Digite o preço : R$"))
print(f"A metade de {moeda.fmoeda(p)} é {moeda.fmoeda(moeda.meio(p))}\nO dobro de {moeda.fmoeda(p)} é {moeda.fmoeda(moeda.dob(p))}\nO aumento de 10% de {moeda.fmoeda(p)} é {moeda.fmoeda(moeda.aumepot(p, 10))}\nReduzindo 13% de {moeda.fmoeda(p)} temos {moeda.fmoeda(moeda.dimpot(p, 13))}"
      f"")