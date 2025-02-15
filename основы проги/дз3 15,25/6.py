for a in range(10**8):
    f = 1
    for x in range(1000):
        for y in range(1000):
            if ((5 * x + 6* y < 121) or (y > a) or (x > a)) == 0:
                f = 0
    if f: print(a)