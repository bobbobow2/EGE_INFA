f = open('5.txt')
a = [int(i) for i in f]
mins3 = min([j for j in a if j % 3 == 0])
count = 0
maxx = -1
for i in range(len(a) - 1):
    if a[i] % mins3 == 0 and a[i+1] % mins3 == 0:
        count += 1
        maxx = max(maxx, a[i] * a[i +1])
print(count,maxx)