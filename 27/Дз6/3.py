f = open('27B_3__3tbdl.txt')
n = int(f.readline())

##перебор
# a = [int(i) for i in f]
# count = 0
# for i in range(n-10):
#     for j in range(i + 10, n):
#         if (a[i] * a[j] % 2 == 0) and abs(a[i] - a[j]) % 980 == 0:
#             count += 1
# print(count) # 2

## ЦАРСКИЙ АЛГОРИТМ
d = 980
s = 10
count = 0
pops = [0] * d
a = [int(f.readline()) for _ in range(10)]
for i in range(n-s):
    x = int(f.readline())
    pops[(a[i % s]) % d] += 1
    # работаем с x
    if (x % 980) % 2 == 0:
        count +=  pops[x % 980]
    a[i % s] = x
print(count) # 2 25274