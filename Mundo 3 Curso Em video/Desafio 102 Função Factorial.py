def fac(n, tt=False):
    from math import factorial
    b = n
    if tt == False:
        return factorial(n)
    elif tt == True:
        for x in range(n, 0, -1):
            b *= x
            if x == 1:
                print(x, end=' = ')
            else:
                print(x, end=' x ')
        return factorial(n)

print(fac(10, tt=True))



