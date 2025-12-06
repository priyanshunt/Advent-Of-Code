d = None
with open("d6.txt", 'r') as f:
    d = [list(x.strip('\n')) for x in f.readlines()]

d = [list(row) for row in zip(*d)]

l = []
l1 = []
sign = ''
for x in d:
    if x.count(' ') == len(x):
        l1.append(sign)
        l.append(l1)
        sign = ''
        l1 = []
    else:
        l1.append(''.join([y for y in x[:-1] if y != ' ']))
        if x[-1] != ' ':
            sign = x[-1]
if len(l1) > 0:
    l1.append(sign)
    l.append(l1)

s = 0
for x in l:
    c = int(x[0])
    sign = x[-1]
    for y in x[1:len(x)-1]:
        if sign == '+':
            c += int(y)
        else:
            c *= int(y)
    s += c

print(s)
