import datetime
da = (datetime.datetime.today()).year
ad = int(input("Em que ano você nasceu?"))
ia = da-ad
if ia <= 9:
    print("Você esta na categoria Mirim")
elif 9 < ia <= 14:
    print("Sua categoria é infantil")
elif 14 < ia <= 19:
    input("Sua categoria é junior")
elif ia == 20:
    print("Sua categoria é senior")
elif ia > 20:
    print("Sua categoria é Master")
print(f"Por sua idade ser: \33[1m{ia}\33[m")

