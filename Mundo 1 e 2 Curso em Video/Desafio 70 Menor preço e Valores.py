soma = con = mb = mb2 = pm = f = 0
print(f"{'--'*20}\nLOJA TO COM A BARRIGA MUITO CHEIA\n{'--'*20}")
while f == 0:
    n = input("Nome do Produto:")
    p = float(input("Preço:"))
    if con == 0:
        mb2 = n
        mb = p
    con += 1
    if p < mb:
        mb2 = n
        mb = p
    if p >= 1000:
        pm += 1
    soma += p
    while True:
        c = int(input("Quer continuar?\n1 - Sim\n2 - Não\nSua Opção:"))
        if c == 1:
            print(f"Proximo produto\n{'--'*30}")
            break
        if c == 2:
            print(f"{'--'*20}\nFIM DO PROGRAMA\n{'--'*20}\nO total da sua compra é R${soma:.2f}\nTemos {pm} produtos que custam mais e R$1000.00\nO produto mais barato foi o {mb2} que custo {mb:.2f}")
            f += 1
            break

