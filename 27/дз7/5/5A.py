f = open('A.txt'); f.readline()
cls =[[] for _ in range(3)]
for _ in range(1998):
    s = f.readline().replace(',', '.')
    xy = list(map(float, s.split()))
    if xy[0] > 25: cls[0].append(xy)
    elif xy[1] > 1: cls[1].append(xy)
    else: cls[2].append(xy)

sy = sx = coord_c = 0

for cl in cls:
    mn = 0
    for s1 in range(len(cl)):
        x1, y1 = cl[s1][0], cl[s1][1]
        rast = 0
        for s2 in range(len(cl)):
            x2,y2 = cl[s2][0], cl[s2][1]
            rast += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

        if rast > mn:
            mn = rast
            coord_c = [x1, y1]
    sx += coord_c[0]/3
    sy += coord_c[1]/3
print(int(sx* 100) , int(sy * 100)) # 1928 471
