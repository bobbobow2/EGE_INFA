from fnmatch import *

for i in range(0, 10**8, 4321):
    if fnmatch(str(i), '8??61*3'):
        print(i, i//4321)
