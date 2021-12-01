l = float(input('Largura da sua parede:'))
a = float(input("Altura da sua parede:"))
ar = l * a
tp = 2
tg = ar / 2
print("Para pintar sua parade, você vai precisar de {:.0f}".format(tg))
print("Area da sua parede:{}m² \nM² por tinta: {}m²".format(ar, tp))
