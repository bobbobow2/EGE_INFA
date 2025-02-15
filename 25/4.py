from fnmatch import *
c = 0
sr = 0
for i in range(0, 10**10, 3798):
    if fnmatch(str(i), '1?57*22'):
        c += 1
        sr += i
print(c, int(sr/c))