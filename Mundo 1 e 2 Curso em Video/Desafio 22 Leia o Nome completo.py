x = input("Seu nome completo:")
s = x.split()
d = ''.join(s)
print(x)
print(x.upper())
print(x.lower())
print("Seu nome tem {} letras".format(len(d)))
print("Seu primeiro nome tem {} de letras".format(len(s[0])))