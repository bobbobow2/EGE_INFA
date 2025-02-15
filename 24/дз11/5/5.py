s = open('5.txt').read()

mx = 0
for j in range(3):
    l = 0
    for i in range(j, len(s), 3):
        if s[i: i+3] in ['UPK', 'KPU']:
            l +=1
            mx = max(mx, l)
        else: l = 0
print(mx*3)
