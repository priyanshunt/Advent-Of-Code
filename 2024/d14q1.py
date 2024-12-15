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

new_data = []
for x in data:
    p = x[0]
    v = x[1]
    new_data.append(((p[0] + v[0] * 100) % 101, (p[1] + v[1] * 100) % 103))

s = [0] * 4
for x in new_data:
    if x[0] < 50 and x[1] < 51:
        s[0] += 1
    elif x[0] < 50 and x[1] > 51:
        s[1] += 1
    elif x[0] > 50 and x[1] < 51:
        s[2] += 1
    elif x[0] > 50 and x[1] > 51:
        s[3] += 1

s1 = 1
for x in s:
    s1 *= x
print(s1)