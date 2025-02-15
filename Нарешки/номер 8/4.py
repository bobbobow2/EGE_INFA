from itertools import *
a = permutations('ДОБРЫНЯ', 6)
cnt = 0
t = [i+j for i in 'ОЫЯ' for j in 'ОЫЯ' if i != j]
for i in a:
    s = ''.join(i)
    if all([j not in s for j in t]) and sum(1 for k in 'ОЫЯ' if k in s) <=2:
        cnt += 1
print(cnt)