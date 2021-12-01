p = float(input("Digite o valor do produto:"))
e1 = int(input("Formas de pagamento \n 1 - Dinheiro/Cheque\n 2 - á vista Cartão\n 3 - 2x no Cartão\n 4 - 3x ou mais no cartão\nEscolha entre as opçoes:"))
if e1 == 1:
    print(f"Você recebera um desconto 10% na compra. \n Preço do produto ficará: R${p*0.9:.2f}")
elif e1 == 2:
    print(f"Você recebera um desconto de 5% na compra. \n Preço do produto ficará: R${p*0.95:.2f}")
elif e1 == 3:
    print(f"Você não sofre taxas de juro.\nFicaram 2 parcelas de R${p/2:.2f}")
elif e1 == 4:
    np = int(input("Escolha o numero de parcelas de 3x á 12x no cartão\nNumero de parcelas que deseja pagar:"))
    print(f"Seu produto recebar 20% de juros no seu valor e ficara R${p*1.2}\nCom {np} parcelas no valor de R${(p*1.2)/np:.2f}")
    if np > 12:
        print("Não é possivel realizar esse parcelamento.\n Recomece a compra")
print("Obrigado pela preferencia".title())