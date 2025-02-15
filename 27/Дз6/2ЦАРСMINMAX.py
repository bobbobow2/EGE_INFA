# ЦАРСКИЙ АЛГОРИТМ
# 86182
f = open('3_27B_pairs__3vnyo.txt')
n = int(f.readline())
maxx = -1
a = [int(f.readline()) for _ in range(67)]
ost_m = [[-1, 10**8] for i in range(876)]
for i in range(n - 67):
    x = int(f.readline())
    ost_m[(a[i % 67]) % 876][0]  = max(ost_m[(a[i % 67]) % 876][0], a[i % 67])
    ost_m[(a[i % 67]) % 876][1] = min(ost_m[(a[i % 67]) % 876][1], a[i % 67])

    if ost_m[x % 876][0] != -1: maxx = max(abs(ost_m[x % 876][0] - x), maxx)
    if ost_m[x % 876][1] != 10**8: maxx = max(abs(ost_m[x % 876][1] - x), maxx)
    a[i % 67] = x
print(maxx)
print(ost_m)# 951336 999516


#951336 999516