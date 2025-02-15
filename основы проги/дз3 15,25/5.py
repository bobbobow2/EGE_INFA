for a in range(1, 10**8):
    f = 1
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((y + 2 * x != 77) or (y > a) or (x> a)) == 0:
                f= 0
    if f: print(a)
