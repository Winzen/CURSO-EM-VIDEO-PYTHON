dl = int(input("Quantos dias você passou com ele alugado:"))
kr = float(input("Quantos quilometros você rodou?"))
pp = (dl * 60) + (kr * 0.15)
print("Orçamentos \n Valor total pelos dias: R${}\n Total pelo quilometros: R${:.2f} \n TOTAL A PAGAR:R${:.2f}".format((dl* 60),(kr * 0.16), pp))