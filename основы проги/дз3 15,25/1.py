for a in range(100000):
    f = 1
    for x in range(1, 100):
        for y in range(1,100):
            if ((x > 15) or (x < 2 * y) or (a > x+y)) ==  False: f = 0

    if f: print(a)

