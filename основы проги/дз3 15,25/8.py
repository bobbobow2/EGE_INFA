for a in range(10**8):
    f = 1
    for x in range(1000):
        for y in range(1000):
            if ((x + y <= 25) or (y <= x +3) or (y >= a)) == 0:
                f = 0
    if f: print(a)