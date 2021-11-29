par = 0,
x = int(input("Digite um valor:")),
if x[0] % 2 == 0:
    par += x
for t in range(1, 4):
    c = int(input("Digite um valor?")),
    x += c
    if c[0] % 2 == 0:
        par += c
par = "".join(str(par).strip("()"))
print(f"{'=='*30}\nOs valores digitados foram: {''.join(str(x).strip('()'))}\nOs valores pares digitados foram {par[2:len(par)]}")
print(f"O valor 9 foi digitado {x.count(9)}° vezes")
print(f"O valor 3 foi digitado na posição {x.index(3)+1}" if 3 in x else "O valor 3 não foi digitado nenhuma vez")
