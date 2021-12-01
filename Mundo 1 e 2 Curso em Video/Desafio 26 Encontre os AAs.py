u = input("Digite uma frase qualquer:").strip()
h = int(len(u))
i = h-1
print("o A aparece pela primeira vez na posição {}º".format(u.lower().find("a")+1))
print("o A aparece {} vezes".format(u.lower().count('a')))
print("O já aparece por na posição {}°".format(u.lower().rfind('a')+1))