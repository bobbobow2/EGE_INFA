f = open('27B__tchy.txt')
n = int(f.readline())

# перебор
# count = 0
# a = [int(i) for i in f]
# for i in range(n-3):
#     for j in range(i + 3, n):
#         if (a[i]*a[j]) % 2 != 0 and (a[i]+ a[j]) % 61 ==0:
#             count += 1
# print(count) # 0


# ЦАРСКИЙ АЛГОРИТМ
d = 61
k = 3
ost = [0] * d
a = [int(f.readline()) for _ in range(k)]
count = 0
for i in range(n-k):
    x = int(f.readline())
    ost[(a[i% k]) % d] += int((a[i% k]) % 2 != 0)
    if x % 2 != 0: count += ost[(d -x % d) % d]
    a[i % k] = x
print(count) # 0 51225
