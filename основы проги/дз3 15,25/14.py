from fnmatch import *
it = ''
for i in range(0, 10**9, 11379):
    s = str(i)
    if fnmatch(s, '3?35*44?'):
        print(s, int(s) //11379)
        it += s + ' ' + str(int(s) //11379) + ' '
print(it)