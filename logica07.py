import math


def dist (x1=0,y1=0,x2=0,y2=0):
    d = (x2-x1)**2 + (y2-y1)**2
    res = math.sqrt(d)
    return res

ponto1 = input().split()
ponto2 = input().split()

# valores do ponto1 x1,x2
x1 = float(ponto1[0])
y1 = float(ponto1[1])

# valores do ponto1 x1,x2
x2 = float(ponto2[0])
y2 = float(ponto2[1])

print(f'{dist(x1, y1,x2,y2):.4f}')
