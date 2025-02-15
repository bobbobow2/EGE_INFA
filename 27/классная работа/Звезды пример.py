f= open('2.txt')
s = f.readline()
a = [[] for i in range(3)]
def f1(x1, x2, y1, y2):
    return ((x2 -x1)**2 + (y2 - y1)**2)**0.5

for i in range(10000):
    s = f.readline().replace(',', '.')
    xy = list(map(float, s.split()))
    if (xy[0] < 3) and (xy[1] < 3):
        a[0].append(xy)
    elif (xy[1] > 7):
        a[1].append(xy)
    else:
        a[2].append(xy)
sx = sy = 0

for k in range(3):
    mn = 10**10
    for j in range(len(a[k])):
        ls = 0
        x1, y1 = a[k][j]
        for i in range(len(a[k])):
            x2, y2 = a[k][i]
            ls += f1(x1, x2, y1, y2)
        if ls < mn:
            mn = ls
            t = a[k][j]
    sx += t[0]
    sy += t[1]
print(int((sx/3) * 10000), int((sy/3) * 10000))





