def func(data):
    a1, a2 = data[0]
    b1, b2 = data[1]
    c1, c2 = data[2]

    x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
    y = (c1 * a2 - c2 * a1) / (b1 * a2 - b2 * a1)

    if int(x) == x and int(y) == y and x < 100 and y < 100:
        return int(x * 3 + y)
    else:
        return 0

d = None
with open("d13q1.txt") as f:
    d = f.read().split('\n')

data = []
for i in range((len(d) + 1) // 4):
    j = i * 4
    d1 = []

    e1 = d[j].split('+')
    x = int(e1[1].split(',')[0])
    y = int(e1[2])
    d1.append((x, y))

    e1 = d[j + 1].split('+')
    x = int(e1[1].split(',')[0])
    y = int(e1[2])
    d1.append((x, y))

    e1 = d[j + 2].split('=')
    x = int(e1[1].split(',')[0])
    y = int(e1[2])
    d1.append((x, y))
    
    data.append(d1)

s = 0
for x in data:
    s += func(x)
print(s)