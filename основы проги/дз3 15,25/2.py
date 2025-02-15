def dell(n, m):
    if n % m == 0: return True;
    else: return False
for a in range(1, 10**8):
    f = 1
    for x in range(1, 1000):
        if ((not(dell(x,a)) and dell(x, 4)) <= (not(dell(x, 9)))) == 0:
            f = 0
    if f: print(a)