f = open('1A.txt')
f.readline()
clusters = [[] for _ in range(2)]

for i in range(1500):
    s = f.readline().replace(',', '.')
    xy = list(map(float, s.split()))
    if xy[1] < 0:
        clusters[0].append(xy)
    else:
        clusters[1].append(xy)

coord_c = 0
sx = sy = 0
for cl in clusters:
    mn = 10 ** 10
    for s1 in range(len(cl)):
        x1, y1 = cl[s1][0], cl[s1][1]
        rast = 0
        for s2 in range(len(cl)):
            x2, y2 = cl[s2][0], cl[s2][1]
            rast += ((x2- x1) ** 2 + (y2 - y1) ** 2)**0.5
        if rast < mn:
            mn = rast
            coord_c = [x1, y1]
    sx += coord_c[0]/2
    sy += coord_c[1]/2
print(int(sx * 1000), int(sy * 1000))


