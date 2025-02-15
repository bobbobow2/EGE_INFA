count = 0
for i in range(28585, 28801):
    if str(i)[-2] == '8':
        count += 1
print(count)