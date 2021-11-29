def isp(a):
     while True:
            y = input(f'{a}').strip()
            if y.isnumeric():
                y = int(y)
                return y
            print('\33[1:31mApenas digite numero inteiro meu amigo!\33[m')

x =isp("Quero pão:")
print(x)