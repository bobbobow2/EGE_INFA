f = open('A.txt'); f.readline()
cls = [[] for _ in range(2)]
for _ in range(2000):
    s = f.readline().replace(',', '.')
    xy = list(map(float, s.split()))
    if xy[0] < 20:
        cls[0].append(xy)
    else:
        cls[1].append(xy)

sx = sy = coord_c = 0
for cl in cls:
    mn = 10**10
    for s1 in range(len(cl)):
        x1, y1 = cl[s1][0], cl[s1][1]
        rast = 0
        for s2 in range(len(cl)):
            x2, y2 = cl[s2][0], cl[s2][1]
            rast += ((x2 -x1) ** 2 + (y2 -y1) ** 2) ** 0.5
        if rast < mn:
            mn =  rast
            coord_c = [x1 , y1]
    sx += coord_c[0]/2
    sy += coord_c[1]/2
print(int(sx*100), int(sy * 100)) # 2157 2188