f = open('6.txt')
s = f.readline()
s = s.replace('A', '*')
s = s.replace('C', '*')
for i in range(len(s) + 1):
    if i * '*' in s:
        print(i)