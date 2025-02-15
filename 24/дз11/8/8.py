s = open('8.txt').read()
l = 0
a = '0123456789'
mx = 0
for i in range(len(s) - 1):
    if (s[i] in a and s[i+1] in a) or (s[i] not in a and s[i+1] not in a):
        l +=1
        mx = max(l, mx)
    else:
        l = 0
print(mx+1)
