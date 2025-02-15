f = open('8.txt')
s= f.readline()
cnt = 0
maxx = -1
numb = 0
for i in range(len(s) -1):
    if s[i] == s[i+1]:
        cnt += 1
    else:
        if cnt >= maxx:
            numb = i - cnt
            maxx = cnt
        cnt = 0
print(numb + 1)



