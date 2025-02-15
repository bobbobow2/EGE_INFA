def per(n):
    s = ''
    while n > 0:
        s = str(n % 5) +  s
        n //= 5
    return s
count = 0
maxx = -1
f = open('2.txt')
a = [int(i) for i in f]
for i in range(len(a) - 1):
    a5 =per(a[i])
    b5 = per(a[i+1])

    if (a5[-1] == "2") or (b5[-1] == "2"):
        count += 1
        maxx = max(maxx, a[i]+a[i + 1])
print(count, maxx)

