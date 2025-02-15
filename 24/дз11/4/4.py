s = open('4.txt').read()
mn = 0
for j in range(3):
    l = 0
    for i in range(j, len(s), 3):
        if s[i:i+3] in ['YZX', "ZXY"]:
            l += 1
            mn = max(mn, l)
        else:
            l = 0
print(mn*3)