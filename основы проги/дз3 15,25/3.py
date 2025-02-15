it = ''
from fnmatch import *
for i in range(0, 10**7,17 ):
    s= str(i)
    if fnmatch(s, '123*4?6'):
        print(s, int(s) // 17)
        it += s+ ' ' + str(int(s) // 17) + ' '
print(it)
print('1230426 72378 1231446 72438 1232466 72498 1233486 72558 1238416 72848 1239436 72908')