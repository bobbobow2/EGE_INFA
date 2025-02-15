count = 0
mx = 10**10

for i in range(3721,7753):
    b_i = bin(i)[2:]
    if i % 3 == 0 and b_i[-3:] != '000':
        count += 1
        mx = min(mx, i)
print(count, mx) #1176 3723