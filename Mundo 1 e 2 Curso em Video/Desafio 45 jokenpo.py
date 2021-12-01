import emoji
import random
import time
e1 = int(input(emoji.emojize("1 - Tesoura :v:\n2 - Pedra :punch:\n3 - Papel :hand:\nDigite sua escolha:", use_aliases=True)))
e2 = random.randint(1, 3)
e3 = ":v:", ":punch:", ":hand:"
t = use_aliases=True
print(emoji.emojize(f"Você escolheu {e3[(e1 - 1)]}", use_aliases=True))
time.sleep(1.5)
print("Resultado é...")
time.sleep(1.5)
print("Jo")
time.sleep(0.5)
print("Ken")
time.sleep(0.5)
print("Po!!!")
time.sleep(0.5)
print("---"*20)
if e1 == e2:
    print("Empate")
    if e1 == 1 and e2 == 1:
        print(emoji.emojize(":v: x :v:", use_aliases=True))
    elif e1 == 2 and e2 == 2:
        print(emoji.emojize(":punch: x :punch:", use_aliases=True))
    elif e1 == 3 and e2 == 3:
        print(emoji.emojize(":hand: x :hand:", use_aliases=True))
if e1 == 1 and e2 == 3:
    print("VOCÊ VENCEU!!!!")
    print(emoji.emojize(f"{e3[0]} x {e3[2]}", t))
if e1 == 2 and e2 == 1:
    print("VOCÊ VENCEU!!!!")
    print(emoji.emojize(f"{e3[1]} x {e3[0]}", t))
if e1 == 3 and e2 == 2:
    print("VOCÊ VENCEU!!!!")
    print(emoji.emojize(f"{e3[2]} x {e3[1]}", t))
if e2 == 1 and e1 == 3:
    print("VOCÊ PERDEU :C")
    print(emoji.emojize(f"{e3[0]} x {e3[2]}", t))
if e2 == 2 and e1 == 1:
    print("VOCÊ PERDEU :C")
    print(emoji.emojize(f"{e3[1]} x {e3[0]}", t))
if e2 == 3 and e1 == 2:
    print("VOCÊ PERDEU :C")
    print(emoji.emojize(f"{e3[2]} x {e3[1]}", t))
