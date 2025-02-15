f = open('2.txt')
s = f.readline()

count = 0
for i in range(len(s)-2):
    if len(set([k for k in s[i: i+ 3]])) < 3 and len(s[i: i+ 3]) == 3:
        count += 1

print(count)