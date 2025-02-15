f = open('И.txt'); f.readline()
cls = [[] for _ in range(4)]
for _ in range(10000):
    s = f.readline().replace(',', '.')
    xy = list(map(float, s.split()))
    if xy[0] < 3.5 and xy[1] > 5.5:
        cls[0].append(xy)
    elif xy[0] < 3.5 and xy[1] < 5.5:
        cls[1].append(xy)
    elif xy[0] > 3.5 and xy[1] < 5.5:
        cls[2].append(xy)
    else:
        cls[3].append(xy)

sy = sx = 0
coord_c = 0
for cl in cls:
    mn = 10**10
    for s1 in range(len(cl)):
        x1, y1 = cl[s1][0], cl[s1][1]
        rast = 0
        for s2 in range(len(cl)):
            x2, y2 = cl[s2][0], cl[s2][1]
            rast += ((x2 -x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        if rast < mn:
            mn = rast
            coord_c = [x1, y1]
    sx += coord_c[0]/4
    sy += coord_c[1]/4
print(int(sx * 100), int(sy * 100)) # 353 548
