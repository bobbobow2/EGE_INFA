f = open('1.txt')
a = [int(i) for i in f]
count = 0
minn= 10**8
for i in range(len(a) - 2):
    if (sum(1 for j in a[i:i+3] if j % 10 == 7) >= 1) and (sum(j for j in a[i : i+3]) % 6 == 0):
        count += 1
        # print(*[j for j in a[i : i+3]])
        if (sum(j for j in a[i : i+3])) < minn:
            minn = sum([j for j in a[i : i+3]])
print(count, minn)

