f = open('27B__tchu.txt')
n=  int(f.readline())

# перребор
# maxx = 0
# a = [int(i) for i in f]
# for i in range(n- 4):
#     for j in range(i+4, n):
#         if (a[i] * a[j]) % 5 == 0:
#             maxx = max(maxx, (a[i] * a[j]))
# print(maxx) # 2321000

## Царский алгоритм
a = [int(f.readline()) for _ in range(4)]
pops = [0, 0]
maxx = 0
for i in range(n-4):
    x = int(f.readline())
    pops[0] = max(pops[0], a[i%4])
    if a[i%4] % 5 == 0: pops[1] = max(pops[1], a[i % 4])
    if x * pops[0] % 5 == 0 and (x * pops[0]) > maxx:
        maxx = x * pops[0]
    elif x * pops[1] % 5 == 0 and (x * pops[1]) > maxx:
        maxx = x * pops[1]
    a[i % 4] = x
print(maxx) # 2321000 99820045