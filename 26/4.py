from math import *

f = open('4.txt')
k_m = int(f.readline())
n_clients = int(f.readline())
och = sorted([list(map(int, f.readline(). split())) for _ in range(n_clients)])

ms = [[] for _ in range(k_m)]
count = 0
last_num = -1 # +1

for start, end in och:
    for k in range(k_m):
        if ms[k] == []:
            if (k + 1) % 5 == 0:
                if (end - start) % 2 ==0:
                    ms[k].append([start, start + round((end - start)/2)])
                    count += 1
                    last_num = k + 1
                    break
                else:
                    ms[k].append([start, start + floor((end - start)/2)])
                    count += 1
                    last_num = k +1
                    break
            else:
                ms[k].append([start, end])
                count += 1
                last_num = k +1
                break

        elif start > ms[k][-1][1]:
            if (k + 1) % 5 == 0:
                if (end - start) % 2 ==0:
                    ms[k].append([start, start + round((end - start)/2)])
                    count += 1
                    last_num = k + 1
                    break
                else:
                    ms[k].append([start, start + floor((end - start)/2)])
                    count += 1
                    last_num = k +1
                    break
            else:
                ms[k].append([start, end])
                count += 1
                last_num = k +1
                break
print(count, last_num)
