import time
import datetime

xa = int(input("Digite o ano que nasceu:"))
#m = int(input("Digite o Mês que Nasceu"))
#xd = int(input("Digite o dia que nasceu:"))
xt = datetime.datetime.now()
rt = (xt.year - xa) - 18
#xtt = datetime.datetime(xa, xm, xd)
print(f"Quem nasceu em {xa} tem {xt.year - xa} anos")
if rt == 0:
    print("Você deve se alistar esse ano")
elif rt > 0:
    print(f"Você esta {rt} ano/s atrasado para se alistar")
elif rt < 0:
    print(f"Ainda falta {int(rt*-1)} ano/s para você se alistar")
if rt >= 0:
    print(f"Seu alistamento vai/foi ser {xt.year - rt}")
if rt < 0:
    print(f"Seu alistamento vai/foi ser {xt.year - (rt)}")

