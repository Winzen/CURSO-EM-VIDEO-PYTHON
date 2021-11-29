def notdic(* m, tt=False):
        g = dict()
        g['total'] = len(m)
        g['maior'] = max(m)
        g['menor'] = min(m)
        g['media'] = sum(m) / len(m)
        if tt == True:
            if g["media"] >= 7:
                g['situação'] = 'APROVADO'
            elif 5 <= g['media'] < 7:
                g['situação'] = "RAzoável".upper()
            elif g['media'] < 5:
                g['situação'] = 'RUIM'
        return g


r = notdic(3.5, 2, 6.5, 2, 7, 4, tt=True)
print(r)