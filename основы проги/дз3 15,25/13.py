from fnmatch import *
it = ''
for i in range(0, 10**11, 17456):
    s = str(i)
    if fnmatch(s, '1?20*24?4'):
        print(s, int(s) //17456)
        it += s + ' ' + str(int(s) //17456) + ' '
print(it)