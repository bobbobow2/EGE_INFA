s = open('7.txt').read()
# s = 'TABCT'
mx = -1
l = 0
for i in range(len(s) - 1):
    if s[i] == 'T':
        if s[i] != s[i+1]:
            l += 1
            mx = max(mx, l)
        else:
            l= 0
    else: l+=1; mx = max(mx, l)
print(mx+1)