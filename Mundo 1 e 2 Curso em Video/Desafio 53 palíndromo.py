r = input("Digite uma frase:").lower().split()
c = "".join(filter(str.isalpha, r))
print(f"O inverso de {c} é {c[::-1]}")
if c == c[::-1]:
    print("Isso é palíndromo")
else:
    print("Isso não é um palindromo")