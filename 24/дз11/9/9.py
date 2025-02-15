s = open('9.txt').read()
c = ''
for i in range(len(s)):
    if i * 'FDE' in s:
        c += i*'FDE'
print(c)
for j in 'FDE':
    if (c + j) not in s:
        print(len(c), c)
    else:
        c += j