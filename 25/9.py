def to11(num):
    s = ''
    while num !=0:
        s = str(num%11) + s
        num //= 11
    return s

for i in range(2031, 14313):
    if '2' not in to11(i):
        mx = i

print(mx)