g = input("Digite uma expressão:")
h = g.count("(") + g.count(")")
print("Sua expressão esta certa!!" if h % 2 == 0 else "Sua Expressão ta errada")