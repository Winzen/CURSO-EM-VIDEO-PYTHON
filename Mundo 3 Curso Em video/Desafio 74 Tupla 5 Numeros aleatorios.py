import random
c = random.randint(0, 500),
for x in range(1, 5):
    u = random.randint(0, 500),
    c += u
print(f"Valores sorteados: {''.join(str(c)).strip(', ()')}")
print(f"Menor valor sorteado: {min(c)}")
print(f"O Maior valor sorteado: {max(c)}")