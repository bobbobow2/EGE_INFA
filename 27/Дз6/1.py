f = open('1A__2pbyi.txt')
n =  int(f.readline())
count = 0
# < => k + 1,  не строго k
# # перебор
# a = [int(k) for k in f]
# # print(a)
# for i in range(n-6):
#     # print(a[i])
#     for j in range(i+6, n):
#         # print(a[i] + a[j])
#         if (a[i] + a[j]) % 210 == 0:
#             count += 1
# print(count)

# ЦАРСКИЙ АЛГОРИТМ
# n_ost = [0] * 210
# a = [int(f.readline()) for _ in range(7)]
# for i in range(n-7):
#     x = int(f.readline())
#     n_ost[a[i%7] % 210] += 1
#     count += n_ost[(210 - (x % 210)) % 210]
#     a[i%7] = x
        # print(count) # 0 238305

# Динамика
n_ost = [0] * 210
a = [int(f.readline()) for i in range(7)]
for i in range(n-7):

    a.append(int(f.readline()))
    # print(a)
    n_ost[a[0] % 210] += 1
    count += n_ost[(210 - (a[7] % 210)) % 210]
    a.pop(0)
print(count) # 0 238305