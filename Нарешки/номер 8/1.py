# a = 'КАЛИЙ'
# a1 = 'КАЛИ'
# cnt = 0
# for i in a1:
#     for j in a:
#         for k in a:
#             for l in a:
#                 for n in a:
#                     s = i + j + k + l + n
#                     if 'ИАК' not in s and len(set([i, j, k ,l ,n])) == 5:
#                         cnt += 1
# print(cnt)

from itertools import *
cnt = 0
a =permutations('КАЛИЙ')
for i in a:
    s = ''.join(i)
    if "ИАК" not in s and (s[0] != 'Й'):
        cnt += 1
print(cnt)