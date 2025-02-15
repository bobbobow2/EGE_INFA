f = open('A.txt'); f.readline()
cls = [[] for _ in range(5)]

for _ in range(1000):
    s = f.readline().replace(',', '.')
    xy = list(map(float, s.split()))
    if xy[0] < -33 and xy[1] > 2.5:
        cls[0].append(xy)
    elif -36 < xy[0] < -18 and -15 < xy[1] < 5:
        cls[1].append(xy)
    elif -18 < xy[0] < 0:
        cls[2].append(xy)
    elif xy[0] * xy[1] < 0:
        cls[3].append(xy)
    else:
        cls[4].append(xy)
coord_c = 0
sx = sy = 0
for cl in cls:
    mn = 10**8
    for s1 in range(len(cl)):
        x1, y1= cl[s1][0], cl[s1][1]
        rast = 0
        for s2 in range(len(cl)):
            x2, y2 = cl[s2][0], cl[s2][1]
            rast += ((x2- x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        if rast < mn:
            mn = rast
            coord_c = [x1, y1]
    sx += coord_c[0]/5
    sy += coord_c[1]/5
print(int(sx * 1000), int(sy * 1000)) # -330 -6530
