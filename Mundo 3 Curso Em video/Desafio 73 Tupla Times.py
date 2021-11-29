t = "Flamengo", "Internacional", "Atlético-MG", "São Paulo", "Fluminense", "Grêmio", "Palmeiras", "Santos", "Athletico-PR",\
    "Bragantino", "Ceará", "Corinthians", "Atlético-GO", "Bahia", "Sport", "Fortaleza", "Vasco", "Goiás", "Coritiba", "Botafogo"
print(t, end= "")
print(f"{'--'*20}\nLista de times do brasileirão: {t}".strip(" ()"))
print(f"{'--'*20}\nOs 5 primeiros são : {t[0:5]}".strip(" ()"))
print(f"{'--'*20}\nOs 4 ultimos são: {t[-4:]}".strip(" ()"))
print(f"{'--'*20}\nTimes em ordem albabética: {sorted(t)}".strip(" []"))
p = str(input(f"{'--'*20}\nDigite um nome para saber a posição dele:"))
print(f"O time do {p} está na posição {(t.index(p)+1)}°")