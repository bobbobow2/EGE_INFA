f = open('7.txt')
s = f.readline()
count = 0
maxx = 0
for i in range(len(s)-1):
    if (s[i] == s[i+1]) and s[i] != 'D':
        count += 1
    else:
        maxx = max(maxx, count)
        count = 0
print(maxx+1) # 5



