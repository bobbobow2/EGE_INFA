f = open('3.txt')
a = [int(i) for i in f]
maxx = max(j for j in a if j % 8 ==0)
mins = 10**8
count = 0
for i in range(len(a)-1):
    if a[i] > maxx or a[i + 1] > maxx:
        count += 1
        mins = min(mins, a[i] + a[i +1])
print(count, mins)
