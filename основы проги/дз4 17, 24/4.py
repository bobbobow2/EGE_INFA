f = open('4.txt')
a  = [int(i) for i in f]
count = 0
maxx = -1
arg = sum(j for j in a if j % 4 == 0) / len([j for j in a if j % 4 == 0])
for i in range(len(a) - 1):
    if a[i] > arg or a[i+1] > arg:
        count += 1
        maxx= max(maxx, a[i] + a[i + 1])
print(count, maxx)
