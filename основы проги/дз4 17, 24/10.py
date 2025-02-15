f= open('10.txt')
s = f.readline()
count = 0
s = s.replace("DRLLRD", "DRL LRD")
s = s.replace('DRL', '*')
s=  s.replace('LRD', "*")
for i in range(len(s)+1):
    if i * '*' in s:
        print(i * 3)