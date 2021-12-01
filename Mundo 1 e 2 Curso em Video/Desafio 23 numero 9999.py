x = int(input("Digite um numero até '9999':"))
c = "{:4}".format(x)
print("Numero digitado:{} \n Unidade:{} \n Dezena:{} \n Centena:{} \n Milhar:{}".format(x,c[3],c[2],c[1],c[0]))