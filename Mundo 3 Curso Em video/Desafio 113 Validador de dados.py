from mundo.dados import dados
try:
    t = dados.isp("Digite um numero inteiro:")
    g = dados.onlyreal("Digite um numero real:")
except SystemExit:
    print("O usuario preferiu não informar dados")

print(f"O valor inteiro digitado foi {t} e o real foi {g}")