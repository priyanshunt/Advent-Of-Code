d = None
with open("d6.txt", 'r') as f:
    d = [x.strip() for x in f.readlines()]

d1 = []
for x in d:
    s = ''
    i = 0
    for y in x:
        if y != ' ':
            s += y
        elif s != '':
            if len(d1) > i:
                d1[i].append(s)
            else:
                d1.append([s])
            s = ''
            i += 1
    if s != '':
        if len(d1) > i:
            d1[i].append(s)
        else:
            d1.append([s])

s = 0
for x in d1:
    c = int(x[0])
    sign = x[-1]
    for y in x[1:len(x)-1]:
        if sign == '+':
            c += int(y)
        else:
            c *= int(y)
    s += c

print(s)
