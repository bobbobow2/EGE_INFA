f = open('1.txt')
s = f.readline()
l = 0
lmax = -1
for i in range(1, len(s)-2, 2):
    s1, s2 = s[i], s[i+2]
    if s[i] == s[i+2] == 'M':
        l += 1
        if l > lmax:
            lmax = l
    else:
        l = 0
print(lmax + 1)


