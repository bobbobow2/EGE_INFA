f = open('3_27A_pairs__3vnyn.txt')
n = int(f.readline())

## перебор
# a = [int(i) for i in f]
# maxx = -10**10
# for i in range(n-67):
#     for j in range(i + 67, n):
#         if abs(a[i] - a[j]) % 876 == 0 and abs(a[i] - a[j]) > maxx:
#             maxx = abs(a[i] - a[j])
# print(maxx) # 951336

# ЦАРСКИЙ АЛГОРИТМ
#86182
f = open('3_27A_pairs__3vnyn.txt')
n = int(f.readline())
maxx = -1
a = [int(f.readline()) for _ in range(67)]
ost_m = [0] * 876
for i in range(n - 67):
    x = int(f.readline())
    ost_m[(a[i % 67]) % 876]  = max(ost_m[a[i % 67] % 876], a[i % 67])
    maxx = max(abs(ost_m[x % 876] - x), maxx)
    a[i % 67] = x
print(maxx) # 996527


#
# # Динамика
# a = [int(i) for i in f]
# ost_m = [0] * 876
# for i in range(n - 67):
#     ost_m[a[i] % 876]  = max(ost_m[a[i] % 876], a[i])
#     s = a[i+67]
#     if abs(ost_m())


