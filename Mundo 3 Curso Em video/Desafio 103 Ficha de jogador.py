def ficha(a='<deconhecido>', b=0):
        if a == '' and b == '':
            a = '<deconhecido>'
            b = 0
        elif a == '':
            a = '<deconhecido>'
        elif b == '':
            b = 0
        return f'O jogador {a} fez {b} gol(s) no campeonato.'

a = str(input("Nome do jogador:"))
b = input("Número de Gols:")
print(ficha(a, b))