count = 0
for i in range(467693, 467741):
    s_c = sum([int(_) for _ in str(i)])
    if i % s_c == 0:
        print(i, end = ' ')
