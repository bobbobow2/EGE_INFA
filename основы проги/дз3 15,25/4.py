count = 0
for i in range(10**4, 20002):
    dels = set()
    for j in range(1, int(i**0.5) + 1):
        if i % j == 0:
            dels.add(j)
            dels.add(i//j)
    if len(dels) == 5:
        count += 1
        print(*sorted(list(dels)))
print(count)