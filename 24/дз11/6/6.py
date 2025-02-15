s = open('6.txt').read()
a =  'QEYUIOAJ'

mx = 0
for j in range(2):
    l = 0
    for i in range(j, len(s)-1, 2):
        if s[i] in a and s[i+1] not in a:
            l +=1
            mx = max(mx, l)
        else:
            l = 0
print(mx)
