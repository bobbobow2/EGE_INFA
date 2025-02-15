f = open('3.txt')
n_pok = int(f.readline())
n_cam = int(f.readline())
och = []
kams = [[[] * n_cam for __ in range(n_cam)] for _ in range(3)]
print(kams)

for j in range(n_pok):
    spec = {'A': 0, 'B': 1, 'C': 2}
    spis = []
    s = f.readline().split()
    spis.append(int(s[0]))
    spis.append(int(s[1]))
    spis.append(spec[s[2]])
    och.append(spis)
count = 0
last_cat = -1
och = sorted(och)
# print(och)
for start, end, ves in och:
    f = 0
    for j in range(ves,3):
        for k in range(n_cam):
            if kams[j][k] == []:
                kams[j][k].append([start, end, ves])
                count += 1
                last_cat = ves
                f = 1
                break
            elif start > kams[j][k][-1][1]:
                kams[j][k].append([start, end, ves])
                count += 1
                last_cat = ves
                f = 1
                break
        if f == 1:
            break
print(count, last_cat) # 273 B