f = open('2.txt')
n = int(f.readline())
k = int(f.readline())
och = [list(map(int, f.readline().split())) for _ in range(n)]
och.sort(key = lambda x: (x[0], x[1]))
camers = [[] for _ in range(k)]
count = 0
last_n = 0
for start, end in och:
    for k_n in range(k):
        if camers[k_n] == []:
            camers[k_n].append([start, end])
            count += 1
            break
        elif start >  camers[k_n][-1][1] + 3:
            camers[k_n].append([start, end])
            count += 1
            last_n = k_n + 1
            break
print(camers) # 155 29
print(count, last_n)