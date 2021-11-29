l = "Pão", 2.50, 'banana', 7.00, 'Tomate', 8.00, 'Lentinha', 9, 'Maça', 150
print(f"{'=-'*25}\n{'Loja Soninho Feliz':^50}\n{'=-'*25}".upper())
for x in range(0, len(l), 2):
    print(f"{l[x]:.<10}{'R$':.>30}{l[x+1]:>9.2f}")