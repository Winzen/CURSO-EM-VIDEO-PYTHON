from mundo.dados import dados
from time import sleep
while True:
    print(f"{'=-'*20}\n{'MENUS PRINCIPAL'.center(40)}\n{'=-'*20}")
    print(f'\33[1:33m1\33[m - \33[1:34mVer pessoas cadastradas\n\33[1:33m2\33[m - \33[1:34mCadastra nova pessoa\n\33[1:33m3\33[m - \33[1:34mSair do Sistema\33[m')
    r = dados.isp(f"{'=-'*20}\n\33[1:33mSuas Opçoes:\33[m")
    sleep(0.5)
    if r <= 3:
        if r == 1:
            print(f"{'=-' * 20}\n{'pessoas cadastradas'.upper().center(40)}\n{'=-' * 20}")
            d = open('teste.txt', 'r')
            print(d.read())
            sleep(0.5)
        elif r == 2:
            d = open('teste.txt', 'a')
            n = input("Nome da pessoa:")
            i = dados.isp("Idade:")
            d.write(f"\n{n:<30}{i:<4}anos")
            sleep(0.5)
        else:
            print("Obrigado!!!!")
            break

