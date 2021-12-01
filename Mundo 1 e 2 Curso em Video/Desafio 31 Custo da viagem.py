x = int(input("Sua viagem terá quantos quilometros?"))
if x <= 200:
    cu = float(x*0.5)
    print(f"Sua viagem de {x}Km, vai custar R${cu}.")
else:
    cuh = float(x*0.45)
    print(f"Sua viagem de {x}km, vai custar R${cuh}")