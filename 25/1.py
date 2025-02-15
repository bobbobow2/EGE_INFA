#
for i in range(0, 10**9, 58598):
    s = str(i)
    if s[0] == '2' and s[3:6] == '656':
        print(i, i // 58598)
# from fnmatch import *
# for i in range(0, 10**9, 58598):
#     if fnmatch(str(i), '2??656*'):
#         print(i, i // 58598) # 272656494 4653