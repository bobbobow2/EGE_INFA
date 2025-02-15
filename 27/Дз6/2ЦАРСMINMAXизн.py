# ЦАРСКИЙ АЛГОРИТМ
# 86182
f = open('3_27B_pairs__3vnyo.txt')
n = int(f.readline())
maxx = -1
a = [int(f.readline()) for _ in range(67)]
ost_m = [[-1, 10**8] for _ in range(876)]
for i in range(n - 67):
    x = int(f.readline())
    ost_m[(a[i % 67]) % 876][0]  = max(ost_m[a[i % 67] % 876][0], a[i % 67])
    ost_m[(a[i % 67]) % 876][1] = min(ost_m[a[i % 67] % 876][1], a[i % 67])
    a[i % 67] = x
    ost_m[x % 876][0]  = max(ost_m[x % 876][0], x)
    ost_m[x % 876][1] = min(ost_m[x % 876][1], x)

for k in range(876):
    if -1 not in ost_m[k] and 10**8 not in ost_m[k]:
        maxx = max(ost_m[k][0] - ost_m[k][1], maxx)
print(maxx) # 951336 999516


#951336 999516