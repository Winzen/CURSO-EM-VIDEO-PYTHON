import math
x = float(input("Complimento do cateto oposto?"))
y = float(input("Complimento do cateto adjacente?"))
print("A hipotenusa vai medir {:.2f}".format(math.hypot(x,y)))
print(math.sqrt((math.pow(x,2)) + (pow(y,2))))