for a in range(10**8):
    f = 1
    for x in range(100):
        for y in range(100):
            for z in range(100):

                if ((z > y) or (y > 30) or (x > 50) or (10 * x + 3 * y - 5 * z < a)) ==0 :
                    f = 0
    if f: print(a)