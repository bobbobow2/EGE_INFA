s = open('10.txt').read()[:-1]
# s = '1-1+1-1+1-1'
s = s.replace('-', '*-')
s = s.replace('+', '*+')
spis = s.split('*')
print(sum(map(float,(spis))))