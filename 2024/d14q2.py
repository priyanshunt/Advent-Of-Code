d = None
with open("d14q1.txt") as f:
    d = f.read().split('\n')

data = []
for x in d:
    d1 = []

    x1 = x.split('=')
    x2 = x1[1].split(',')
    d1.append((int(x2[0]), int(x2[1].split(' ')[0])))

    x2 = x1[2].split(',')
    d1.append((int(x2[0]), int(x2[1])))
    
    data.append(d1)

p, v = zip(*data)
p, v = list(p), list(v)
for i in range(1, 10001):
    for j in range(len(v)):
        p[j] = ((p[j][0] + v[j][0]) % 101, (p[j][1] + v[j][1]) % 103)

    q = sorted(p)
    t = 0
    prev = (-1, -1)
    for j in range(len(q)):
        x = q[j]
        if x[0] == prev[0] and x[1] == prev[1] + 1:
            t += 1
        else:
            t = 0
        prev = x
        if t > 20:
            pattern = ''
            for k in range(103):
                for l in range(101):
                    if (l, k) in p:
                        pattern += '#'
                    else:
                        pattern += '.'
                pattern += '\n'
            print(pattern)
            print(i)
            exit()