from mundo.moeda import moeda

p = float(input("Digite o preço : R$"))
print(f"A metade de {moeda.fmoeda(p)} é {moeda.meio(p)}\nO dobro de {p} é {moeda.dob(p)}\nO aumento de 10% de {p} é {moeda.aumepot(p, 10)}\nReduzindo 13% de {p} temos {moeda.dimpot(p, 13)}"
      f"")