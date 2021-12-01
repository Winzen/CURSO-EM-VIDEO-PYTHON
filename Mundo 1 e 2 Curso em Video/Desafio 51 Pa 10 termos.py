pt = int(input("Primeiro termo da PA:"))
r = int(input("Razão da PA:"))
for f in range(pt, (pt+(10-1)*r)+r, r):
    print(f, end=" ")