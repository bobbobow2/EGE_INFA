def dels(n):
    dels = set()
    for k in range(2, int(i**0.5) + 1):
        if n % k == 0:
            dels.add(k)
            dels.add(n // k)
    dels = list(dels)
    if len(dels) ==  4 and sum(i % 2 for i in dels) == 2:
        return True
    return False
count = 0
summa = 0
for i in range(90000, 147000 + 1):
    if dels(i):
        count += 1
        summa += i
print(str(count)+str(summa))