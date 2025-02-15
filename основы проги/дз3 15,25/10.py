count = 0
for i in range(1111, 555556):
    dels = set()
    for j in range(1,int( i ** 0.5) + 1):
        if i % j == 0:
            dels.add(j)
            dels.add(i // j)
    if len(dels) % 2 == 0:
        count += 1
print(count)