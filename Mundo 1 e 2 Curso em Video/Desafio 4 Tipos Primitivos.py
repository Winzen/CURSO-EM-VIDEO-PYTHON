c = input("Digite algo:")
print("O tipo premitivo desse valor é {}".format(type(c)))
print('è numetico? {}'.format(c.isnumeric()))
print("È alfabetico? {}".format(c.isalpha()))
print("Está em máisculas?{}".format(c.isupper()))
print("Está em minúsculas? {}".format(c.islower()))
print("Está capitalizada? {}".format(c.istitle()))
print("Tem espaço? {}".format(c.isspace()))