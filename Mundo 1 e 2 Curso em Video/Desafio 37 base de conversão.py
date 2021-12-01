print("\33[1:34m1\33[m - Para \33[1:36mBinaria\33[m\n\33[1:34m2\33[m - Para \33[1:35mOctal\33[m\n\33[1:34m3\33[m - Para \33[1:33mHexadecimal\33[m ")
print("--"*20)
x = int(input("\33[1:34mEscolha a base da conversão entre as opçoes:\33[m"))
if x == 1:
    print("Você escolheu a base \33[1:34mBinaria\33[m")
    y = int(input("Qual numero você gostaria de converter:"))
    print("---" * 20)
    print(f"Seu numero em \33[1:34mBinario\33[m fica: \33[1:34m{y:b}\33[m")
elif x == 2:
    print("Você escolheu a base \33[1:35mOctal\33[m")
    y = int(input("Qual numero você gostaria de converter:"))
    print("---"*20)
    print(f"Seu numero em \33[1:35mOctal\33[m fica: \33[1:35m{y:o}\33[m")
elif x == 3:
    print("Você escolheu base \33[1:33mHexadecimal\33[m")
    y = int(input("Qual numero você gostaria de converter:"))
    print("---" * 20)
    print(f"Seu numero em \33[1:33mHexadecimal\33[m fica: \33[1:33m{y:x}\33[m")





