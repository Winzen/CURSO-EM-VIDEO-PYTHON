def hep(a):
    from time import sleep
    print(f"\33[1:31:40m{'=-' * 20}\nACESSANDO O MANUAL DO COMANDO 'INPUT'\n{'=-' * 20}")
    sleep(0.5)
    print(f'\33[m\33[1:32:40m')
    help(a)
    print('\33[m ')
    sleep(1)

while True:
    print(f"\33[1:34:40m{'=-'*20}\n        SISTEMA DE AJUDA PyHELP\n{'=-'*20}")
    f = input(f"\33[mPara parar digite 'fim'\nFUNCÂO OU BIBLIOTECA:")
    if f == 'fim':
        print('ATÈ LOGO')
        break
    hep(f)
