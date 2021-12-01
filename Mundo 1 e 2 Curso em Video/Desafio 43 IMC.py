print("\33[1:34mCalculo De IMC \33[m ")
print("____"*30)
p = float(input("Digite seu peso:"))
a = float(input("Sua altura:"))
i = p / a**2
if i < 18.5:
    print("Você esta abaixo do peso")
elif 25 > i >= 18.5:
    print("Você esta no peso ideal!")
elif 25 <= i < 30:
    print("Você esta acima do peso.")
elif 30 <= i < 40:
    print("Você esta obeso")
elif i >= 40:
    print("Você esta em obesidade morbida")
print(f"Seu IMS é:{i:.1f}")