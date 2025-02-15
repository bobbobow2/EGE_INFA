f = open('1.txt')
n = int(f.readline())
och =[list(map(int, f.readline().split())) for _ in range(n)]
och.sort(key = lambda x: (x[1], x[0]))
zal = []
minute = [0] * 1440

for start, end in och:
    if zal == []:
        zal.append([start, end])
        for i in range(start, end+1):
            minute[i] = 1
    elif start >= zal[-1][1]:
        zal.append([start, end])
        for i in range(start, end+1):
            minute[i] = 1
print(sorted([i for i in och if i[0] > zal[-2][1]]))
print((len(zal))) # 40 26
print(zal[-2][1])
print(1299 - 1273)