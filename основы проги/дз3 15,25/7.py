for a in range(10**8):
    f = 1
    for x in range(1000):
        for y in range(1000):
            if ((7 * x + 2 * y >= a) or (x <= 20) or (y < 52)) == 0:
                f = 0
    if f: print(a)