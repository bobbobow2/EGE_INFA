def prost(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num  % i == 0:
            return False
    return True and (num != 1)
summa = 0

for num in range(131590, 591585):
    if prost(num):
        summa += sum([int(_) for _ in str(num)])
print(summa) # 948492